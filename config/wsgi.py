# task_manager_backend/config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Ensure this matches your settings folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()