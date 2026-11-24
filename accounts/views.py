from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer,UserSerializer
from rest_framework.generics import CreateAPIView
from  .models import User

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


# class RegisterView:
#     pass