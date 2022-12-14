from django.shortcuts import render
from cms.models import Blog


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog_list(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog-list.html', context)