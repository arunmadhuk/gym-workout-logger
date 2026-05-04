from gym_app.models import *
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.conf import settings
import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active',
                   'created_at', 'updated_at', 'last_login', 'groups', 'user_permissions']


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class WorkoutSessionSerializer(ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = WorkoutSession
        fields = ['session_id', 'user_details', 'session_date', 'start_time', 'end_time',
                  'duration_minutes', 'calories_burned', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['session_id',
                            'duration_minutes', 'created_at', 'updated_at']

    def validate(self, data):
        """Additional validation"""
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError({
                'end_time': 'End time must be after start time'
            })

        return data


class ExerciseLogSerializer(ModelSerializer):

    workout_session_details = WorkoutSessionSerializer(
        source='workout_session', read_only=True)
    exercise_details = ExerciseSerializer(source='exercise', read_only=True)

    class Meta:
        model = ExerciseLog
        fields = [
            'log_id', 'workout_session', 'workout_session_details',
            'exercise_details', 'sets_completed', 'reps_completed',
            'weight_kg', 'duration_minutes', 'notes',
            'created_at', 'updated_at'
        ]
