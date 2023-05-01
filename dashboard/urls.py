from . import views
from django.urls import path


urlpatterns = [
    path('profile/', views.loadProfilePage, name='profile'),
    path('editprofile/<str:pk>', views.editProfile, name='editprofile'),
]