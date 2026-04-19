from django.urls import path
from api_app.views.exercise import *
from api_app.views.workout import *

urlpatterns = [
    path('exercise/', ExerciseAPIView.as_view(), name='exercise-api-view'),
    path('exercise-logs/user/<int:user_id>/', UserExerciseLogsAPIView.as_view(), name='user-exercise-logs-api-view'),
    path('exercise-logs/user/<int:user_id>/<str:session_date>/', UserExerciseLogsAPIView.as_view(), name='user-exercise-logs-session-date'),
    path('exercise-logs/date/<str:session_date>/', DatewiseExerciseLogsAPIView.as_view(), name='exercise-logs-by-date-api-view'),
    path('workout/',WorkoutSessionAPIView.as_view(), name='workout-api-view'),
    path('workout/list/',WorkoutSessionsListAPIView.as_view(), name='workout-list-create-api-view'),
]   