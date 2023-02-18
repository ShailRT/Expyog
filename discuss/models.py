from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Query(models.Model):
    query_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    category = models.CharField(max_length=40)
    body = models.TextField()
    image = models.ImageField(upload_to='question/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_user')
    assigned_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='assigned_user',null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    up_vote = models.ManyToManyField(User, related_name='upvote')
    down_vote = models.ManyToManyField(User, related_name='downvote')
    date_created = models.DateTimeField(auto_now_add=True)

    query = models.ForeignKey(Query, on_delete=models.CASCADE)




    
