from typing import Optional
from django.contrib.auth import authenticate
from django.contrib.auth import models  # Import models from Django's auth
from rest_framework.views import APIView  # Corrected import
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class UserLogin(APIView):
    def post(self, request):
        password = request.data.get('password')
        username = request.data.get('username')
        
        user: Optional[models.User] = authenticate(
            username=username,
            password=password,
        )
        
        if not user:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_404_NOT_FOUND
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key},
            status=status.HTTP_201_CREATED
        )

class UserProfile(APIView):
    def get(self, request):
        pass