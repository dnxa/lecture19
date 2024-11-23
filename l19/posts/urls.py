from django.urls import path
from .views import create_posts, main_posts

urlpatterns = [
    path('', main_posts, name="main_posts"),
    path('create/', create_posts, name="create_posts")
]