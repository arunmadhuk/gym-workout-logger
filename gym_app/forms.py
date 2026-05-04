from django import forms
from django.forms import inlineformset_factory
from requests import request
from .models import ExerciseLog, WorkoutSession, Exercise, User


class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        exclude = ['duration_minutes']


class ExerciseLogForm(forms.ModelForm):
    workout_session = forms.ModelChoiceField(
        queryset=WorkoutSession.objects.all(),
        label='Workout Session',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(),
        label='Exercise',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sets_completed = forms.IntegerField(min_value=1, label='Sets Completed', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reps_completed = forms.IntegerField(min_value=1, label='Reps Completed', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight_kg = forms.FloatField(min_value=0, label='Weight (kg)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    distance_km = forms.FloatField(min_value=0, label='Distance (km)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    duration_minutes = forms.IntegerField(min_value=0, label='Duration (minutes)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(label='Notes', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))   

    class Meta:
        model = ExerciseLog
        fields = ['workout_session', 'exercise', 'sets_completed', 
                  'reps_completed', 'weight_kg', 'distance_km', 'duration_minutes', 'notes']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        print(f"Initializing ExerciseLogForm with user: {user}")
        super().__init__(*args, **kwargs)
        if user:
            workout_sessions = WorkoutSession.objects.filter(
            user=user
            ).exclude(
            # Exclude sessions that have any exercise logs
            session_id__in=ExerciseLog.objects.filter(
                workout_session__user=user
            ).values_list('workout_session_id', flat=True).distinct()
            )
            self.fields['workout_session'] = forms.ModelChoiceField(
                queryset=workout_sessions,
                label='Workout Session',
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        else:
            self.fields['workout_session'] = forms.ModelChoiceField(
                queryset=WorkoutSession.objects.none(),
                label='Workout Session',
                widget=forms.Select(attrs={'class': 'form-control'})
            )


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'


# Create formset for exercise logs
ExerciseLogFormSet = inlineformset_factory(
    WorkoutSession, 
    ExerciseLog, 
    form=ExerciseLogForm,
    extra=1
)
