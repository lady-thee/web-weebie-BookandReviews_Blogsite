from django.shortcuts import render, redirect
from .models import BlogPost, Tags
from .forms import BlogForm


def loadCreatePostPage(request):
    # blogform = BlogForm()
    context = {
        'has_error': False,
        'data': request.POST,
    }
    
    if request.method == 'POST':
        title = request.POST['post_title']
        image = request.FILES.get('post_image')
        # image = request.FILES['post_image']
        add_tag = request.POST.getlist('genre')
        body = request.POST['post_body']

        print(title,image,add_tag)
        try:
            blog = BlogPost(post_title=title, post_image=image, post_body=body)
            # for tag in range(len(add_tag)):
            #     blog.tags.add(add_tag[tag])
            t_tags = Tags.objects.get(tag='fantasy')
            print(add_tag[0])
            if t_tags == (add_tag[0]):
                return True
            print(t_tags)
            # blog.tags_set.add()

            
            # blog.save()
            # all_tags = Tags.objects.all()
            # all_tags = list(all_tags)
            # for tag in range(len(all_tags)):
            #     # print(tag)
            #     pretag = all_tags[tag]
            #     for x in range(len(add_tag)):
            #         print(add_tag[x])
            #         if add_tag[x] in all_tags:
            #             print('yes')
            #         else:
            #             print('no')

                # print(pretag, type(pretag))
                
                
            # blog.save()
        except ValueError:
            print('Something is wrong')
        
    return render(request, 'blogpages/create.html', context)


def loadPostsPage(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts, 
    }
    return render(request, 'blogpages/posts.html', context)


def loadPostPage(request, pk):
    post = BlogPost.objects.get(id=pk)
    # tags = BlogPost.tags.all()
    # comments = BlogPost.votes_total

    context = {
        'post': post,
        # 'tags': tags,
    }

    return render(request, 'blogpages/post.html', context)


