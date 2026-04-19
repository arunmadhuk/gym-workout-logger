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


class ExercisePagination(PageNumberPagination):
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
    
class UserExerciseLogsAPIView(ListAPIView):
    serializer_class = ExerciseLogSerializer
    pagination_class = ExercisePagination

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
    

class DatewiseExerciseLogsAPIView(ListAPIView):
    serializer_class = ExerciseLogSerializer
    pagination_class = ExercisePagination

    def get(self,request, session_date=None):
        print(f"get request received for user exercise logs - {session_date} {request.query_params}")
        
        if WorkoutSession.objects.filter(session_date=session_date).exists() is False:
            return Response(
                {'error': 'No workout sessions found for the specified date'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        exercise_log_qs = ExerciseLog.objects.filter(workout_session__session_date=session_date).order_by('-created_at')
        print(f"Initial exercise log queryset - {exercise_log_qs}")

        paginator = self.pagination_class()
        paginated_exercise_log = paginator.paginate_queryset(exercise_log_qs, request)
        serializer = self.get_serializer(paginated_exercise_log, many=True)

        return Response({
            'data': serializer.data,
            'total_count': exercise_log_qs.count(),
            'page_number': paginator.page.number,
            'session_date': session_date,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }, status=status.HTTP_200_OK)