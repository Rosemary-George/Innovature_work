# Create your views here.


# Create your views here.

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.views import APIView
from .serializers import TokenObtainPairSerializer
from Authentication.models import CustomUser
from Authentication.serializers import UserSerializer, TokenObtainPairSerializer



class CustomTokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


def index(request):
	return render(request,'index.html')

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# class CustomTokenObtainPairView(generics.CreateAPIView):
#     serializer_class = TokenObtainPairSerializer
#     permission_classes = [permissions.AllowAny]


class TokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenRefreshView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
def post(self, request, *args, **kwargs):
    serializer = TokenObtainPairSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    refresh_token = serializer.validated_data.get('refresh')
    return Response({'refresh': str(refresh_token)})
