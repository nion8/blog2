# from django.db import models
from django.db import models
from user_profile.models import User

# Create your models here.
from django import forms

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=31, default='Global')
    is_active = models.BooleanField(default=True)
    is_favorit = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:48]

    # email = models.EmailField()
    # name = models.CharField(max_length=128)

