from . import views
from django.urls import path


urlpatterns = [
    path('create post/', views.loadCreatePostPage, name='create'),
    path('posts/', views.loadPostsPage, name='posts'),
    path('post/<str:pk>', views.loadPostPage, name='post'),
]