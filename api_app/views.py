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


class ExerciseAPIView(APIView):
    serializer_class = ExerciseSerializer

    def get(self, request, exercise_id=None):
        context = {}
        if exercise_id:
            exercise = Exercise.objects.get(exercise_id = exercise_id)
            print(f"Exercise request of {exercise_id} is {exercise}")
            context['exercise'] = exercise
        
        print(f"get request - {context}")
        return Response(context, status=200) 

    def post(self, request):
        print(f"post request received - {request}")
        return Response({}, status=201)
    

class WorkoutSessionAPIView(APIView):
    serializer_class = WorkoutSessionSerializer
    pagination_class = WorkoutPagination

    def get(self, request, user_id=None, session_date=None):

        if not user_id:
            return Response(
                {'error': 'User ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(user_id=user_id).exists() is False:
            return Response(
                {'error': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        if WorkoutSession.objects.filter(user__user_id=user_id, session_date=session_date).exists() is False:
            return Response(
                {'error': f'No workout sessions found for the user on the given date - {session_date}'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        user_qs = User.objects.get(user_id=user_id)
        workout_qs = WorkoutSession.objects.filter(user=user_qs, session_date=session_date)
        
        serializer = self.serializer_class(workout_qs, many=True)

        return Response({
            'data': serializer.data,
            'count': workout_qs.count(),
            'user_id': user_id,
            'session_date': session_date
        }, status=status.HTTP_200_OK)


class UserWorkoutSessionAPIView(ListAPIView):
    serializer_class = WorkoutSessionSerializer
    pagination_class = WorkoutPagination

    def get(self,request, user_id=None):
        print(f"get request received for user workout session - {user_id} {request.query_params}")
        if not user_id:
            return Response(
                {'error': 'User ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user_qs = User.objects.get(user_id=user_id)

        if User.objects.filter(user_id=user_id).exists() is False:
            return Response(
                {'error': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        if WorkoutSession.objects.filter(user__user_id=user_id).exists() is False:
            return Response(
                {'error': 'No workout sessions found for the user'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        workout_qs = WorkoutSession.objects.filter(user=user_qs).order_by('-session_date', '-start_time')

        paginator = self.pagination_class()
        paginated_workout = paginator.paginate_queryset(workout_qs, request)
        serializer = self.get_serializer(paginated_workout, many=True)

        return Response({
            'data': serializer.data,
            'total_count': workout_qs.count(),
            'page_number': paginator.page.number,
            'user_id': user_id,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }, status=status.HTTP_200_OK)



class WorkoutSessionCreateAPIView(CreateAPIView):
    serializer_class = WorkoutSessionSerializer

    def create(self, request):
        print(f"post request received for workout session - {request.data}")
        serializer = self.serializer_class(data=request.data)
        print(f"serializer is valid - {serializer.is_valid()} , errors - {serializer.errors}")
        if serializer.is_valid():
            workout_session = serializer.save()
            return Response({
                'message': 'Workout session created successfully',
                'session_id': workout_session.session_id
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserExerciseLogsAPIView(ListAPIView):
    serializer_class = ExerciseLogSerializer
    pagination_class = WorkoutPagination

    def get(self,request, user_id=None, session_date=None):
        print(f"get request received for user exercise logs - {user_id} {request.query_params}")
        if not user_id:
            return Response(
                {'error': 'User ID is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if User.objects.filter(user_id=user_id).exists() is False:
            return Response(
                {'error': 'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        if WorkoutSession.objects.filter(user__user_id=user_id).exists() is False:
            return Response(
                {'error': 'No workout sessions found for the user'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        exercise_log_qs = ExerciseLog.objects.filter(workout_session__user_id=user_id).order_by('-created_at')
        print(f"Initial exercise log queryset - {exercise_log_qs}")

        if session_date:
            print(f"Filtering exercise logs for session date - {session_date}")
            exercise_log_qs = ExerciseLog.objects.filter(workout_session__user_id=user_id, workout_session__session_date=session_date).order_by('-created_at')

        print(f"Filtered exercise log queryset - {exercise_log_qs}")

        paginator = self.pagination_class()
        paginated_exercise_log = paginator.paginate_queryset(exercise_log_qs, request)
        serializer = self.get_serializer(paginated_exercise_log, many=True)

        return Response({
            'data': serializer.data,
            'total_count': exercise_log_qs.count(),
            'page_number': paginator.page.number,
            'user_id': user_id,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }, status=status.HTTP_200_OK)