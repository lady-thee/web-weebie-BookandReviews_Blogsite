from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        pass
        if not email:
            raise ValueError('Email must be given!')
        
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', False)
        # kwargs.setdefault('')

        user = self.model(
            email = self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email must be given')
        
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)


        superuser = self.model(
            email = self.normalize_email(email),
            **kwargs
        )
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser

        
        





class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    email = models.EmailField(db_index=True, unique=True, max_length=280, verbose_name='Email of any user')
    created_time = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    last_login = models.DateField(auto_now_add=True)


    class Meta:
        unique_together = ['id', 'email']


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email 
    
    def has_perms(self, perm, obj=None):
        return self.is_superuser
    
    def get_full_name(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return True
    



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    firstname = models.CharField(max_length=200, verbose_name='the first name of a user', blank=True, null=True)
    lastname = models.CharField(max_length=200, verbose_name='the last name of a user', blank=True, null=True)
    display_pic = models.ImageField(upload_to='photo/%Y/%m/%d', default='static/images/avatar.jpg', blank=True, null=True, verbose_name='profile picture')
    bio = models.TextField(blank=True, null=True, verbose_name='bio of user')


    def __str__(self):
        self.full = self.lastname + ' ' + self.firstname
        return str(self.full)
    



    

