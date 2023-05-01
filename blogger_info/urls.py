from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.registerUsers, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate_token, name='activate'),
    path('login/', views.loginUsers, name='login')
]