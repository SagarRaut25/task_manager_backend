from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# The router automatically creates /tasks/ and /tasks/<id>/
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]