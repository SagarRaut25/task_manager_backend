from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserCreate

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='api_register'),
]