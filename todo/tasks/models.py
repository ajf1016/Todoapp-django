from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'tasks_tasks'

    def __str__(self):
        return self.title
