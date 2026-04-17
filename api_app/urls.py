from django.urls import path
from api_app.views import *

urlpatterns = [
    path('exercise/', ExerciseAPIView.as_view(), name='exercise-api-view'),
    path('workout/',WorkoutSessionCreateAPIView.as_view(), name='workout-api-view'),
    path('workout/<int:user_id>/<str:session_date>/', WorkoutSessionAPIView.as_view(), name='workout-session-detail'),
    path('workout/<int:user_id>/', UserWorkoutSessionAPIView.as_view(), name='user-workout-session-api'),
]