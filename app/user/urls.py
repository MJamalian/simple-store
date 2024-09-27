from django.urls import path
from user.views import (
    CreateUserAPIView,
    LoginUserAPIView,
)

app_name = "user"

urlpatterns = [
    path("signup/", CreateUserAPIView.as_view(), name="signup"),
    path("login/", LoginUserAPIView.as_view(), name="login")
]
