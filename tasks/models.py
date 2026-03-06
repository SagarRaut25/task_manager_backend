# tasks/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # This ForeignKey links every task to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed'] # Shows uncompleted tasks first