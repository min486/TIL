from django.db import models

class Todo(models.Model):
  content = models.CharField(max_length=80)
  completed = models.BooleanField(default=False)
  priority = models.IntegerField(default=3)
  deadline = models.DateField(null=True)
  created_at = models.DateField(auto_now_add=True)