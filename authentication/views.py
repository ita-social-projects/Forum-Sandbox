from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomUserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
