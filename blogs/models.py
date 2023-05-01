from django.db import models
from blogger_info.models import Profile 
import uuid



class BlogPost(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key='True', editable=False)
    post_title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Title of blog post')
    post_image = models.ImageField(upload_to='posts/%Y/%m/%d', default='static/images/avatar.jpg', blank=True, null=True, verbose_name='Blog post picture')
    tags = models.ManyToManyField('Tags', blank=True,  verbose_name='Tags seperated by #')
    post_body = models.TextField(blank=True, null=True, verbose_name='body of user')
    created_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.post_title
    


class Tags(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    tag = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.tag



class Comments(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    comment_body = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, primary_key=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.value,' ', self.blogpost)
