from django.db import models

# Create your models here.

class TodoItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    priority = models.CharField(max_length=6, blank=False)
    
    def __str__(self):
        return self.name

