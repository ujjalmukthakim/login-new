from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.

class RegisterView(ModelViewSet):
    queryset=User
    serializer_class=RegisterSerializer
