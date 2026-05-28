from django.shortcuts import render
from gym_app.forms import ExerciseForm, ExerciseLogForm
from gym_app.models import ExerciseLog
from django.contrib import messages
from django.shortcuts import redirect
from gym_app.models import Exercise, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

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
            'distance_km': request.POST.get('distance_km'),
            'duration_minutes': request.POST.get('duration_minutes'),
            'description': request.POST.get('description'),
            'name':request.POST.get('name'),
        }
        print(f"Data to be validated: {data}")
        if not Exercise.objects.filter(name=data['name'],exercise_type=data['exercise_type'], equipment=data['equipment'], difficulty=data['difficulty']).exists():
            form = ExerciseForm(data)
            if form.is_valid():
                form.save()
                print("Form is valid. Exercise would be saved to the database.")
                msg = f"{data['name']} created succesfully"
                return JsonResponse({
                'status': 'success',
                'message': msg,
                }, status=201)
            else:
                print("Form is invalid. Errors:")
                print(form.errors)
                msg = f"{data['name']} creation failed"
                return JsonResponse({
                    'status': 'error',
                    'message': msg
                }, status=500)
        else:
            print("An exercise with the same name, exercise type, equipment, and difficulty already exists.")
            form = ExerciseForm(data)
            form.add_error(None, "An exercise with the same date and time already exists.")
            context['form'] = form
            msg = f"An exercise with the same name - {data['name']} and exercise type - {data['exercise_type']}, equipment - {data['equipment']}, difficulty - {data['difficulty']} already exists."
            return JsonResponse({
                    'status': 'error',
                    'message': msg
                }, status=409)
   
    return render(request, template_name, context)

@login_required
def edit_exercise(request, exercise_id):
    print(f"Edit exercise view called for exercise_id: {exercise_id}")
    exercise = Exercise.objects.filter(exercise_id=exercise_id).first()
    print(f"Exercise retrieved from database: {exercise}")
    if not exercise:
        messages.error(request, 'Exercise not found.')
        return redirect('exercise-list')
    
    template_name = 'exercise/edit.html'
    context = {'title': 'Edit Exercise', 'button_text': 'Update Exercise', 'button_color': 'warning'}
    form = ExerciseForm(instance=exercise)
    context['form'] = form
    context['exercise'] = exercise

    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        print("ExerciseForm submitted with data:")
        print(f"Exercise ID: {exercise_id}")
        print(f"Exercise Data: {form.data}")
        print(f"Is form valid? {form.is_valid()}")
        print(f"Form errors: {form.errors if not form.is_valid() else 'No errors'}")
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise updated successfully!')
            return redirect('exercise-list')
        else:
            messages.error(request, 'Please correct the errors below.')
            context['form'] = form
            return render(request, template_name, context)

    return render(request, template_name, context)

@login_required
def exercise_list(request):
    exercises = Exercise.objects.all().order_by('-created_at')
    context = {
        'exercises': exercises
    }
    return render(request, 'exercise/exercise_list.html', context)
