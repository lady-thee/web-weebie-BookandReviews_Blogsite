from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Profile, Users
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.conf import settings

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generator_token

from django.core.mail import EmailMessage
import time 




def registerUsers(request):
    context1 = {
        'data': request.POST,
        'has_error': False,
        }
    # context2 = {
    #     'error': 'Email already exists!',

    # }
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('password2')
        bio = request.POST.get('bio')
        image = request.FILES.get('pic')
        # if len(request.FILES) != 0:
        #     images = request.FILES
        #     image = images['pic']
        # print(firstname, lastname, email, password, bio)
        if password == confirmpass:
            if Users.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                context1['has_error']=True

            else:
                predata = Users.objects.create_user(
                    email = email,
                    password = password
                )

                
                profile_data = Profile(user=predata, firstname=firstname, lastname=lastname, bio=bio, display_pic=image)
                profile_data.save()
                predata.save()
                
                messages.success(request, 'Successfully created account')
                time.sleep(2)
                messages.info(request, 'Check your email inbox or spam to verify account')

                # time.sleep(4)
                sendActivationMail(predata, request)



    return render(request, 'auth_pages/signup.html', context1)




def sendActivationMail(user, request):
    current_site = get_current_site(request)
    email_subject = 'Verify your account'
    # context = {
    #     'click_action': 'showDomainLink',
    # }
    email_body = render_to_string(
        'mail_temp/confirm_temp.html',
        {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generator_token.make_token(user),
        }, 
        # context 
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()




def activate_token(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Users.objects.get(pk=uid)
    except (ValueError, Users.DoesNotExist):
        user = None
    
    if user is not None and generator_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Successfully verified email')
        return redirect(reverse('login'))
    else:
        messages.error(request, 'Verification link was invalid')
        return redirect(reverse('index'))




def loginUsers(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        upass = request.POST['password']

        user = authenticate(request, email=email, password=upass)
        if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful')
                    time.sleep(2)
                    return redirect(reverse('index'))  
        else: 
            messages.error(request, 'Invalid user')
            return redirect(reverse('login'))
        
    return render(request, 'auth_pages/login.html', context)


# def logoutUser(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'You are logged out')
#         return redirect('index')
