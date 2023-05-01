from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout, user_logged_out
from django.contrib.auth.decorators import login_required

import time

from blogger_info.models import Users, Profile


def loadIndexPage(request):
    context = {}
    print(request.user.is_authenticated)
    return render(request, 'pages/index.html', context)


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You are logged out')
        return redirect(reverse('login'))

# def logoutUser(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         url = reverse('blogger_info:login')
#         print(request)
#         # messages.success(request, 'You are logged out')
#         # time.sleep(2)
#         # return redirect(url, args=(), kwargs={})
#         return 
    
    
