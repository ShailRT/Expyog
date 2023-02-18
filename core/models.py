from django.db import models
from django.contrib.auth.models import User
from discuss.models import Query, Comment

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=12,blank=True, null=True)
    email = models.CharField(max_length=120,blank=True, null=True)
    website = models.CharField(max_length=120,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    speciality = models.CharField(max_length=200,null=True,blank=True)
    questions = models.PositiveIntegerField(default=0)
    answers = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.user.username

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['type']
    
    def __str__(self):
        return f"{self.type} - {str(self.approved)}"