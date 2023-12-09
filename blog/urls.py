from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('blogs/', views.Posts, name='blogs'),
    path('users/', views.users, name='users'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blogs/details/<int:ID>', views.blogdetails, name='blogdetails'),
]