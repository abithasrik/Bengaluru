from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model
from rest_framework.permissions import AllowAny,IsAuthenticated
import re

User = get_user_model()





@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    identifier = request.data.get('username')  # Can be username or email
    password = request.data.get('password')

    if not identifier or not password:
        return Response({'error': 'Username or email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Determine if identifier is an email
    if re.match(r"[^@]+@[^@]+\.[^@]+", identifier):
        try:
            user = User.objects.get(email=identifier)
            username = user.username
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        username = identifier

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key,
        'user_id': user.id,
        'username': user.username,
        'email': user.email
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
