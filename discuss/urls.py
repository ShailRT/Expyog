from django.urls import path 
from . import views 

urlpatterns = [
    path('create', views.create_question, name="create-question"),
    path('detail/<str:pk>/', views.detail_question, name="detail-question"),
    path('upvote/', views.upvote, name="upvote"),
    path('downvote/', views.downvote, name="downvote"),
]
