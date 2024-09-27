from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

# Create your views here.

class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer

class LoginUserAPIView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
