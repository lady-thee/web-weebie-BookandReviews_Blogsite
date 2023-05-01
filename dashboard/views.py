from django.shortcuts import render, redirect 
from blogger_info.models import Profile, Users

def loadProfilePage(request):
    # user = Profile.objects.get(pk)
    # if request.user.
    
    context = {
        "current_user" : request.user,
    }
    return render(request, 'dashpages/dash.html', context)


def editProfile(request, pk):
    user_info = Profile.objects.get(id=pk)
    context = {
        'uid': user_info,
    }
    old_firstname = user_info.firstname
    old_lastname = user_info.lastname
    old_photo = user_info.display_pic
    old_bio = user_info.bio
    old_email = user_info.user.email 
    if request.method == 'POST':
        if ('firstname' in request.POST) and ('bio' in request.POST) and ('lastname' in request.POST) and ('email' in request.POST):          
           user_info.user.email = request.POST.get('email')
           user_info.firstname = request.POST.get('firstname')
           user_info.lastname = request.POST.get('lastname')
           user_info.bio = request.POST.get('bio')

           user_info.user.save()
           user_info.save()
           
        elif 'profile_pic' in request.FILES:
          
           user_info.display_pic = request.FILES.get('profile_pic')
           user_info.save()
        


    # print(old_email, old_firstname, old_lastname, old_photo)

    return render(request, 'dashpages/editdash.html', context)