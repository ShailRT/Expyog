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
    path('ques/', views.question, name="question"),
    path('account/sign-up', views.sign_up, name="sign-up"),
    path('account/edit-profile/', views.edit_profile, name="edit-profile"),
    path('account/profile/<str:pk>/', views.user_profile, name="profile"),
    path('account/user-question/', views.user_question, name="user-question"),
    path('question-assign/<str:pk>/', views.question_assignment, name="question-assign"),
    path('account/user-question-list/', views.user_question_list, name="user-question-list")

]
