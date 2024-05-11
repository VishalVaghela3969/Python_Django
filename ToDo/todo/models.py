from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}: due {self.due_date}"