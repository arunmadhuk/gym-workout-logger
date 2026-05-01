from django.shortcuts import render
from gym_app.forms import WorkoutForm
from gym_app.models import WorkoutSession, User
from django.contrib.auth.decorators import login_required


@login_required
def create_workout_session(request):
    print("Create workout session view called")
    print(f"Request : {request}")
    template_name = 'workout/create.html'
    context = {'title': 'Create Workout Session', 'button_text': 'Create Session', 'button_color': 'success'}
    if request.method == 'POST':
        print("WorkoutForm submitted with data:")

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
            form = WorkoutForm(data)
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
            form = WorkoutForm(data)
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