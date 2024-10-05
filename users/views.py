from django.shortcuts import render

from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics


class UserCreate(generics.CreateAPIView):
    """Вьюшка создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

