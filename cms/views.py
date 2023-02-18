from django.shortcuts import render
from .models import Blog

def blog_detail(request, pk):
    blog = Blog.objects.filter(slug=pk).first()

    context = {
        'blog': blog,
    }
    
    return render(request, 'blog.html', context)




