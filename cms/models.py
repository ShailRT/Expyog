from django.db import models
from ckeditor.fields import RichTextField 

class Blog(models.Model):
    title = models.CharField(max_length=120)
    intro = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    blog_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blog')
    body = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    blog = models.ManyToManyField(Blog)

    def __str__(self):
        return self.title