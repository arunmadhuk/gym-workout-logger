from django.urls import path
from .views.views import dashboard
from .views.workout import create_workout_session, workout_session_list
from .views.auth import user_login, user_logout
from .views.exercise import create_exercise, exercise_list, exercise_log_list, exercise_log_create

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('workout/create/', create_workout_session, name='workout-session-create'),
    path('workout/list/', workout_session_list, name='workout-session-list'),
    path('exercise/create/', create_exercise, name='exercise-create'),
    path('exercise/list/', exercise_list, name='exercise-list'),
    path('exercise/logs/', exercise_log_list, name='exercise-logs-list'),
    path('exercise/logs/create/', exercise_log_create, name='exercise-logs-create'),
]