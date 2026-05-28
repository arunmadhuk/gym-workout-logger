from django.urls import path, re_path
from .views.views import dashboard
from .views.workout import create_workout_session, workout_session_list, edit_workout_session
from .views.auth import user_login, user_logout
from .views.exercise import create_exercise, exercise_list, edit_exercise

from .views.ajax import load_selected_exercise_ajax,load_selected_workout_ajax

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(
    url='/static/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', dashboard, name='dashboard'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),

    # Workout session URLs
    path('workout/create/', create_workout_session, name='workout-create'),
    path('workout/edit/<int:session_id>/', edit_workout_session, name='workout-edit'),
    path('workout/list/', workout_session_list, name='workout-session-list'),

    # Exercise URLs
    path('exercise/create/', create_exercise, name='exercise-create'),
    path('exercise/edit/<int:exercise_id>', edit_exercise, name='exercise-edit'),
    path('exercise/list/', exercise_list, name='exercise-list'),

    # AJAX endpoint
    path(r'load-selected-exercise-ajax/', load_selected_exercise_ajax, name='load-selected-exercise-ajax'),
    path(r'load-selected-workout-ajax/', load_selected_workout_ajax, name='load-selected-workout-ajax'),
]