from django.conf import settings
from api_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Retrieve All workout sessions or by session_id, or filtered by user, date or both.",
        manual_parameters=[
            openapi.Parameter(
                'user_id',
                openapi.IN_QUERY,
                description="User ID (required to filter workouts by user)",
                type=openapi.TYPE_INTEGER,
                required=False
            ),
        ]
    )

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        if user_id:
            print(f"Filtering users by user_id: {user_id}")
            self.queryset = self.queryset.filter(user_id=user_id)
            if not self.queryset.exists():
                return Response({"detail": "No users found for the given user_id."}, status=status.HTTP_404_NOT_FOUND)

        return super().get(request, *args, **kwargs)