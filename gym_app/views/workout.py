from django.shortcuts import get_object_or_404, render
from gym_app.forms import WorkoutSessionForm, ExerciseLogFormSet
from gym_app.models import WorkoutSession, User, Exercise
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def create_workoutsession(request):
    print("Create workout session view called")
    print(f"Request : {request}")
    template_name = 'workout/create.html'
    context = {'title': 'Create Workout Session', 'button_text': 'Create Session', 'button_color': 'success'}
    if request.method == 'POST':
        print("WorkoutSessionForm submitted with data:")

        user = User.objects.filter(email=request.user.email).first()
        print(f"User retrieved from database: {user}")
        data = {
            'user': user,
            'session_date': request.POST.get('session_date'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time'),
            'calories_burned': request.POST.get('calories_burned'),
            'notes': request.POST.get('notes'),
        }
        print(f"Data to be validated: {data}")
        if not WorkoutSession.objects.filter(user=user, session_date=data['session_date'], start_time=data['start_time'], end_time=data['end_time']).exists():
            form = WorkoutSessionForm(data)
            if form.is_valid():
                form.save()
                print("Form is valid. Workout session would be saved to the database.")
            else:
                print("Form is invalid. Errors:")
                print(form.errors)
                context['form'] = form
                return render(request, template_name, context)
        else:
            print("A workout session with the same user, date, start time, and end time already exists.")
            form = WorkoutSessionForm(data)
            form.add_error(None, "A workout session with the same date and time already exists.")
            context['form'] = form
            return render(request, template_name, context)

   
        context['message'] = 'Workout session created successfully!'
    return render(request, template_name, context)


@login_required
def workout_session_list(request):
    workout_sessions = WorkoutSession.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'workout_sessions': workout_sessions
    }
    return render(request, 'workout/list.html', context)


@login_required
def create_workout_session(request):
    """
    Combined view for creating WorkoutSession with ExerciseLogs
    """
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST)
        formset = ExerciseLogFormSet(request.POST)
        print("Received POST data for workout session creation:")
        print(request.POST)
        print(f"WorkoutSession Form valid: {form.is_valid()}, ExerciseLogFormSet valid: {formset.is_valid()}")
        print("WorkoutSession Form errors:", form.errors)
        print("ExerciseLogFormSet errors:", formset.errors)
        if form.is_valid() and formset.is_valid():
            # Save the workout session
            # workout_session = form.save(commit=False)
            # workout_session.user = request.user
            # workout_session.save()
            
            # # Save the exercise logs
            # exercise_logs = formset.save(commit=False)
            # for log in exercise_logs:
            #     log.workout_session = workout_session
            #     log.save()
            
            messages.success(request, f'Workout session saved successfully! Duration: {form.cleaned_data["duration_minutes"]} minutes')
            return redirect('workout-session-list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WorkoutSessionForm()
        formset = ExerciseLogFormSet()

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
    
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, instance=workout_session)
        formset = ExerciseLogFormSet(request.POST, instance=workout_session)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Workout session updated successfully!')
            return redirect('workout_session_detail', session_id=workout_session.session_id)
    else:
        form = WorkoutSessionForm(instance=workout_session)
        formset = ExerciseLogFormSet(instance=workout_session)
    
    context = {
        'form': form,
        'formset': formset,
        'title': 'Edit Workout Session',
        'workout_session': workout_session,
    }
    return render(request, 'workout/create_workout_session.html', context)