from django.db import models

# Create your models here.

class Todo(models.Model):
    rank = models.IntegerField(default=3)
    todo = models.CharField(max_length=80)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    status = models.BooleanField(default=False)