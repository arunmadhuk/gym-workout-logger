from django import forms
from .models import ExerciseLog, WorkoutSession, Exercise, User


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        exclude = ['duration_minutes']


class ExerciseLogForm(forms.ModelForm):
    class Meta:
        model = ExerciseLog
        fields = '__all__'


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
