from django.shortcuts import render
from gym_app.forms import ExerciseForm, ExerciseLogForm
from gym_app.models import ExerciseLog
from django.contrib import messages
from django.shortcuts import redirect
from gym_app.models import Exercise, User
from django.contrib.auth.decorators import login_required


@login_required
def create_exercise(request):
    print("Create exercise view called")
    print(f"Request : {request}")
    template_name = 'exercise/create.html'
    context = {'title': 'Create Exercise', 'button_text': 'Create Exercise', 'button_color': 'success'}
    form = ExerciseForm()
    context['form'] = form
    if request.method == 'POST':
        print("ExerciseForm submitted with data:")

        user = User.objects.filter(email=request.user.email).first()
        print(f"User retrieved from database: {user}")
        data = {
            'exercise_type': request.POST.get('exercise_type'),
            'equipment': request.POST.get('equipment'),
            'difficulty': request.POST.get('difficulty'),
            'sets': request.POST.get('sets'),
            'reps': request.POST.get('reps'),
            'weight_kg': request.POST.get('weight_kg'),
            'duration_minutes': request.POST.get('duration_minutes'),
            'description': request.POST.get('description'),
        }
        print(f"Data to be validated: {data}")
        if not Exercise.objects.filter(exercise_type=data['exercise_type'], equipment=data['equipment'], difficulty=data['difficulty']).exists():
            form = ExerciseForm(data)
            if form.is_valid():
                form.save()
                print("Form is valid. Exercise would be saved to the database.")
            else:
                print("Form is invalid. Errors:")
                print(form.errors)
                context['form'] = form
                return render(request, template_name, context)
        else:
            print("An exercise with the same user, exercise type, equipment, and difficulty already exists.")
            form = ExerciseForm(data)
            form.add_error(None, "An exercise with the same date and time already exists.")
            context['form'] = form
            return render(request, template_name, context)

   
        context['message'] = 'Exercise created successfully!'
    return render(request, template_name, context)


@login_required
def exercise_list(request):
    exercises = Exercise.objects.all().order_by('-created_at')
    context = {
        'exercises': exercises
    }
    return render(request, 'exercise/exercise_list.html', context)

@login_required
def exercise_log_list(request):
    exercise_logs = ExerciseLog.objects.filter(
        workout_session__user=request.user
    ).select_related('workout_session', 'exercise').order_by('-created_at')
    print(f"Retrieved {exercise_logs.count()} exercise logs for user {request.user.email}")
    context = {
        'exercise_logs': exercise_logs
    }
    return render(request, 'exercise/exercise_log_list.html', context)

@login_required
def exercise_log_create(request):
    if request.method == 'POST':
        form = ExerciseLogForm(request.POST)
        if form.is_valid():
            exercise_log = form.save()
            messages.success(request, f'Exercise log for {exercise_log.exercise.name} created successfully!')
            return redirect('exercise-logs-list')
    else:
        form = ExerciseLogForm()
    
    context = {
        'form': form,
        'title': 'Add Exercise Log',
        'button_text': 'Save Exercise Log',
        'button_color': 'primary'
    }
    return render(request, 'exercise/exercise_log_form.html', context)