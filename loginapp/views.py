from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .serializer import UserSerializer
from .models import User

# Create your views here.
class UserView(APIView):
    def home(request):
        return JsonResponse({'message': 'Welcome to the API home page'})

class SignupView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"Login attempt: username={username}, password={password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticate returned: {user}, type: {type(user)}")
        try:
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                print(f"Token: {token.key}, Created: {created}")
                return Response({"message": "Login successful", "token": token.key}, status=200)
            else:
                print("Invalid credentials")
                return Response({"error": "Invalid credentials"}, status=400)
        except Exception as e:
            print(f"Exception during token creation: {e}")
            return Response({"error": str(e)}, status=500)

