# task_manager_backend/tasks/views.py
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer

# 1. User Registration View
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # Anyone can register

# 2. Login View (Returns a Token)
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# 3. Task CRUD ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This ensures you only see tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This attaches the user ID to the task when it's saved
        serializer.save(user=self.request.user)