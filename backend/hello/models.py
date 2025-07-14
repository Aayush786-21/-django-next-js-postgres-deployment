from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ['-created_at']
