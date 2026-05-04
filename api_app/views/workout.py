from django.conf import settings
from api_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination


class WorkoutPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class WorkoutSessionsListAPIView(ListAPIView):
    serializer_class = WorkoutSessionSerializer
    pagination_class = WorkoutPagination

    @swagger_auto_schema(
        operation_description="Retrieve All workout sessions or by session_id, or filtered by user, date or both.",
        manual_parameters=[
            openapi.Parameter(
                'session_id',
                openapi.IN_QUERY,
                description="Session ID (required to filter workouts by specific session)",
                type=openapi.TYPE_INTEGER,
                required=False
            ),
            openapi.Parameter(
                'user_id',
                openapi.IN_QUERY,
                description="User ID (required to filter workouts by user)",
                type=openapi.TYPE_INTEGER,
                required=False
            ),
            openapi.Parameter(
                'session_date',
                openapi.IN_QUERY,
                description="Session date (YYYY-MM-DD) Filter workouts by specific date",
                type=openapi.TYPE_STRING,
                format='date',
                required=False
            ),

        ]
    )
    def get(self, request):
        user_id = request.query_params.get('user_id')
        session_date = request.query_params.get('session_date')
        session_id = request.query_params.get('session_id')
        print(f"get request received for workout session - user_id: {user_id} , session_date: {session_date} , session_id: {session_id} , query_params: {request.query_params}")

        workout_qs = WorkoutSession.objects.all()

        if user_id:
            if User.objects.filter(user_id=user_id).exists() is False:
                return Response(
                    {'error': 'User not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            workout_qs = workout_qs.filter(user__user_id=user_id)

            if session_date:
                if WorkoutSession.objects.filter(user__user_id=user_id, session_date=session_date).exists() is False:
                    return Response(
                        {'error': f'No workout sessions found for the user on the given date - {session_date}'},
                        status=status.HTTP_404_NOT_FOUND
                    )

                workout_qs = workout_qs.filter(session_date=session_date)

        if session_date and not user_id:
            if WorkoutSession.objects.filter(session_date=session_date).exists() is False:
                return Response(
                    {'error': f'No workout sessions found for the given date - {session_date}'},
                    status=status.HTTP_404_NOT_FOUND
                )

            workout_qs = workout_qs.filter(session_date=session_date)

        if session_id:
            if WorkoutSession.objects.filter(session_id=session_id).exists() is False:
                return Response(
                    {'error': f'Workout session not found for the given ID - {session_id}'},
                    status=status.HTTP_404_NOT_FOUND
                )
            workout_qs = workout_qs.filter(session_id=session_id)

        paginator = self.pagination_class()
        paginated_workout_sessions = paginator.paginate_queryset(
            workout_qs, request)
        serializer = self.serializer_class(
            paginated_workout_sessions, many=True)
        paginated_response = paginator.get_paginated_response(serializer.data)

        return Response({
            'data': paginated_response.data,
            'count': workout_qs.count(),
            'user_id': user_id,
            'session_date': session_date,
            'session_id': session_id,
            'page_number': paginator.page.number,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }, status=status.HTTP_200_OK)


class WorkoutSessionAPIView(APIView):
    serializer_class = WorkoutSessionSerializer

    @swagger_auto_schema(
        request_body=WorkoutSessionSerializer
    )
    def post(self, request):
        print(f"post request received for workout session - {request.data}")
        serializer = self.serializer_class(data=request.data)
        print(
            f"serializer is valid - {serializer.is_valid()} , errors - {serializer.errors}")
        if serializer.is_valid():
            # workout_session = serializer.save()
            return Response({
                'message': 'Workout session created successfully',
                'session_id': 'workout_session.session_id'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'session_id',
                openapi.IN_QUERY,
                description="Session ID of the workout to update all fields (required)",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=WorkoutSessionSerializer
    )
    def put(self, request):
        session_id = request.query_params.get('session_id')
        print(
            f"patch request received for workout session - {session_id} , {request.data}")

        if not session_id:
            return Response(
                {'error': 'Session ID is required for updating workout session'},
                status=status.HTTP_400_BAD_REQUEST
            )
        print(
            f"put request received for workout session - {session_id} , {request.data}")
        workout_session_qs = WorkoutSession.objects.get(session_id=session_id)
        if WorkoutSession.objects.get(session_id=session_id) is False:
            return Response(
                {'error': 'Workout session not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(
            workout_session_qs, data=request.data, partial=False)
        print(
            f"serializer is valid - {serializer.is_valid()} , errors - {serializer.errors}")
        if serializer.is_valid():
            workout_session = serializer.save()
            return Response({
                'message': 'Workout session updated successfully',
                'session_id': workout_session.session_id
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'session_id',
                openapi.IN_QUERY,
                description="Session ID of the workout to partially update (required)",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description="Partial update - only include fields to change",
            properties={
                'start_time': openapi.Schema(type=openapi.TYPE_STRING, format='time'),
                'end_time': openapi.Schema(type=openapi.TYPE_STRING, format='time'),
                'calories_burned': openapi.Schema(type=openapi.TYPE_INTEGER),
                'session_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'notes': openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    def patch(self, request):
        session_id = request.query_params.get('session_id')
        print(
            f"patch request received for workout session - {session_id} , {request.data}")
        if not session_id:
            return Response(
                {'error': 'Session ID is required for updating workout session'},
                status=status.HTTP_400_BAD_REQUEST
            )

        workout_session_qs = WorkoutSession.objects.get(session_id=session_id)
        print(workout_session_qs)
        if WorkoutSession.objects.get(session_id=session_id) is False:
            return Response(
                {'error': 'Workout session not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(
            workout_session_qs, data=request.data, partial=True)
        print(
            f"Data to update - {serializer.initial_data} , existing workout session data - {WorkoutSessionSerializer(workout_session_qs).data}")
        print(
            f"serializer is valid - {serializer.is_valid()} , errors - {serializer.errors}")
        if serializer.is_valid():
            workout_session = serializer.save()
            return Response({
                'message': 'Workout session updated successfully',
                'session_id': workout_session.session_id
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific workout session by ID",
        manual_parameters=[
            openapi.Parameter(
                'session_id',
                openapi.IN_QUERY,
                description="Session ID of the workout to delete (required)",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ]
    )
    def delete(self, request):
        session_id = request.query_params.get('session_id')
        if not session_id:
            return Response(
                {'error': 'Session ID is required for deleting workout session'},
                status=status.HTTP_400_BAD_REQUEST
            )
        print(f"delete request received for workout session - {session_id}")
        workout_session_qs = WorkoutSession.objects.get(session_id=session_id)
        if workout_session_qs.exists() is False:
            return Response(
                {'error': 'Workout session not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        workout_session_qs.delete()
        return Response({
            'message': 'Workout session deleted successfully',
            'session_id': session_id
        }, status=status.HTTP_200_OK)
