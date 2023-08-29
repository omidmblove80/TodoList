from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Task(models.Model):
    title = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['start_time',]
