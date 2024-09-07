from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

User = get_user_model()  # This retrieves your custom User model

# SignUp API
@api_view(['POST'])
def sign_up(request):
    data = request.data

    # Check if the email already exists
    if User.objects.filter(email=data['email']).exists():
        return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Create user using the custom manager from your model
    user = User.objects.create_user(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password'],  # Password will be hashed by the manager
    )
    
    user.save()

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


# SignIn API
@api_view(['POST'])
def sign_in(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    # Authenticate the user
    user = authenticate(request, email=email, password=password)

    if user is not None:
        # Create JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
