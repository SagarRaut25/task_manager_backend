from django.contrib import admin
from django.urls import path, include
from tasks.views import CustomAuthToken # We created this in the last step

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This is the endpoint the Frontend will call to Login
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
    
    # This includes all our Task CRUD routes
    path('api/', include('tasks.urls')),
]