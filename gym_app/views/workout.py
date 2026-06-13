import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from gym_app.forms import WorkoutSessionForm, ExerciseLogFormSet, ExerciseLogForm
from gym_app.models import ExerciseLog, WorkoutSession, User, Exercise
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def workout_session_list(request):

    exercise_logs = ExerciseLog.objects.filter(
        workout_session__user=request.user
    ).select_related('workout_session', 'exercise').order_by('-workout_session__session_date', '-workout_session__start_time')
    print(f"Retrieved {exercise_logs.count()} exercise logs for user {request.user.email}")

    context = {
        'exercise_logs': exercise_logs
    }

    return render(request, 'workout/workout_session_list.html', context)


@login_required
def create_workout_session(request):
    """
    Combined view for creating WorkoutSession with ExerciseLogs
    """
    if request.method == 'POST':
        print("Received POST data for workout session creation:")
        print(request.POST)
        data = json.loads(request.body)  # Parse JSON
        workout_data = data.get('workout_data')
        workout_data['user'] = request.user  # Set the user for the workout session
        exercise_data = data.get('exercise_data')
        print("Workout Data:", workout_data)
        print("Exercise Data:", exercise_data)

        form = WorkoutSessionForm(workout_data)
        # formset = ExerciseLogFormSet(, form_kwargs={'user': request.user})
        print("Received POST data for workout session creation:")
        print(request.POST)
        print(f"WorkoutSession Form valid: {form.is_valid()}")
        print("WorkoutSession Form errors:", form.errors)

        if form.is_valid():
            workout_session = form.save(commit=False)
            workout_session.save()
            qs = WorkoutSession.objects.get(session_id=1)
            exercise_data['workout_session'] = workout_session
            exercise_data['exercise'] = Exercise.objects.get(name=exercise_data['exercise_name'])
            exercise_log_form = ExerciseLogForm(exercise_data)
            print(f"ExerciseLogForm valid: {exercise_log_form.is_valid()}")
            print("ExerciseLogForm errors:", exercise_log_form.errors)
            if exercise_log_form.is_valid():
                print("Both forms are valid. Saving workout session and exercise log.")
                # Save the workout session
                exercise_log_form.save()
          
            messages.success(request, f'Workout session saved successfully! Duration: {form.cleaned_data["duration_minutes"]} minutes')
            return redirect('workout-session-list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WorkoutSessionForm()
        formset = ExerciseLogFormSet(  form_kwargs={'user': request.user})

    # Get all exercises for the template (for creating new exercise logs)
    
    exercises = Exercise.objects.all().order_by('name')
    context = {
        'form': form,
        'formset': formset,
        'exercises': exercises,
        'title': 'Log New Workout Session',
    }
    return render(request, 'workout/create_workout_session.html', context)


@login_required
def edit_workout_session(request, session_id):
    """
    Edit existing workout session with its exercise logs
    """
    workout_session = get_object_or_404(WorkoutSession, session_id=session_id, user=request.user)
    exercise_logs = ExerciseLog.objects.filter(workout_session=workout_session).first()
    if request.method == 'POST':
        print("Received POST data for workout session updation:")
        data = json.loads(request.body)  # Parse JSON
        workout_data = data.get('workout_data')
        workout_data['user'] = request.user  
        exercise_data = data.get('exercise_data')
        exercise_data['workout_session'] = workout_session
        exercise_data['exercise'] = Exercise.objects.get(name=exercise_data['exercise_name'])
        print("Workout Data:", workout_data)
        print("Exercise Data:", exercise_data)

        form = WorkoutSessionForm(workout_data, instance=workout_session)
        formset = ExerciseLogForm(exercise_data, instance=exercise_logs)
        print(f"session_id ID: {session_id}")
        print(f"workout Data: {form.data}")
        print(f"Is form valid? {form.is_valid()}")
        print(f"Form errors: {form.errors if not form.is_valid() else 'No errors in form'}")
        
        print(f"Is formset valid? {formset.is_valid()}")
        print(f"formset errors: {formset.errors if not formset.is_valid() else 'No errors in formset'}")
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Workout session updated successfully!')
            return redirect('workout-session-list')
        else:
            errors = {}
            if form.errors:
                errors['workout_errors'] = form.errors
            if formset.errors:
                errors['exercise_errors'] = formset.errors
            if form.non_field_errors():
                errors['non_field_errors'] = form.non_field_errors()
          
            error_fields = list(form.errors.keys()) + list(formset.errors.keys())
            errors['error_fields'] = error_fields
            
            return JsonResponse(errors, status=400)
    else:
        form = WorkoutSessionForm(instance=workout_session)
        exercise_form = ExerciseLogForm(instance=exercise_logs)
            
        print(f"Editing WorkoutSession ID: {session_id}")
        print(f"Initial workout session data: {form.initial}")
        print(f"Initial exercise logs data: {exercise_form.initial }")
    exercises = Exercise.objects.all().order_by('name')
    context = {
        'form': form,
        'exercise_form': exercise_form,
        'exercises': exercises,
        'title': 'Edit Workout Session',
        'workout_session': workout_session,
        'session_id':session_id
    }
  
    return render(request, 'workout/edit_workout_session.html', context)