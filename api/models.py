from django.db import models

# Create your models here.

class TodoList(models.Model):
    PRIORITIES = {
        "1":"Low",
        "2":"Medium",
        "3":"High"
    }

    title = models.CharField(max_length=30)
    description = models.TextField()
    priority= models.CharField(max_length=1,choices=PRIORITIES,default=PRIORITIES["1"])
    is_completed=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

class Tags(models.Model):
    title  = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)