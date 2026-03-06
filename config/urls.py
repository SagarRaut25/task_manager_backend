from django.contrib import admin
from django.urls import path, include
from tasks.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth Endpoints
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
    
    # Task and Registration Endpoints
    path('api/', include('tasks.urls')),
]