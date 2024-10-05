from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreate

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('create/', UserCreate.as_view(), name='create')
]