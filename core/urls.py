from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('contact-us/', views.contact, name="contact"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('blog-list/', views.blog_list, name="blog-list"),
]
