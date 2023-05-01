from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutUser, name='logout'),
    path('', views.loadIndexPage, name='index'),
]
