from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Goal(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title