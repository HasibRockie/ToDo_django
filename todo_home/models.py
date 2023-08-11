from django.db import models

# Create your models here.
class ToDoModels(models.Model):
    taskId = models.AutoField(primary_key=True)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle