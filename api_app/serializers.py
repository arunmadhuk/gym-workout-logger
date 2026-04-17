from gym_app.models import *
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.conf import settings
import requests 
from rest_framework.views import APIView
from rest_framework.response import Response 


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class WorkoutSessionSerializer(ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = "__all__"
        read_only_fields = ['session_id', 'duration_minutes', 'created_at', 'updated_at']


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
    class Meta:
        model = ExerciseLog
        fields = "__all__"
