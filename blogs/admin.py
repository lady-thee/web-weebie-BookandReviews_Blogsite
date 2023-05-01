from django.contrib import admin
from .models import BlogPost, Tags, Comments


admin.site.register(BlogPost)
admin.site.register(Tags)
admin.site.register(Comments)
