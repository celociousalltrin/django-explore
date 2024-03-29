from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

# Create your models here.

class Tags(models.Model):
    title  = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
        
class TodoList(models.Model):
    PRIORITIES = [
     ("low","Low"),
     ("medium","Medium"),
     ("high","High")
    ]

    title = models.CharField(max_length=30)
    description = models.TextField()
    priority= models.CharField(max_length=6,choices=PRIORITIES,default="low")
    is_completed=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    date=models.DateField(default=date.today())
    created_at = models.DateTimeField(auto_now_add=True) 
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, blank=True, related_name="tag")

    def __str__(self):
        return self.title

