from django.urls import path, re_path
from .views.views import dashboard
from .views.workout import create_workout_session, workout_session_list, edit_workout_session
from .views.auth import user_login, user_logout
from .views.exercise import create_exercise, exercise_list, exercise_log_detail, exercise_log_list, exercise_log_create, edit_exercise
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(
    url='/static/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', dashboard, name='dashboard'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    # path('workout/create/', create_workoutsession, name='workout-session-create'),
    path('workout/list/', workout_session_list, name='workout-session-list'),
    path('exercise/create/', create_exercise, name='exercise-create'),

    path('exercise/<int:exercise_id>/edit/', edit_exercise, name='exercise-edit'),
    path('exercise/list/', exercise_list, name='exercise-list'),
    path('exercise/logs/', exercise_log_list, name='exercise-logs-list'),
    path('exercise/logs/create/', exercise_log_create, name='exercise-logs-create'),
    path('workout/create/', create_workout_session, name='workout-session-create'),
    path('workout/<int:session_id>/edit/', edit_workout_session, name='edit_workout'),
    path('exercise_log_detail/<int:log_id>/', exercise_log_detail, name='exercise-log-detail'),
]