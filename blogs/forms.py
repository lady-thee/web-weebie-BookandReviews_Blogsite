from django.forms import ModelForm, widgets
from django import forms
from .models import BlogPost, Comments



class BlogForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_image', 'tags', 'post_body']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super(BlogForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})


# class CommentForm(ModelForm):

#     class Meta:
#         model = Comments
#         fields = ['value', 'comment_body']


#         labels = {
#             'value':'Place your votes',
#             'comment_body': 'Leave your comment',
#         }