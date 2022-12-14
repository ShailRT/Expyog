from django.urls import path 
from . import views 

urlpatterns = [
    path('<str:pk>/', views.blog_detail, name="blog-detail"),
]
