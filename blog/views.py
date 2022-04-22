from django.shortcuts import render,get_object_or_404
from django.views import generic

from blog.admin import PostAdmin
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post
def post_list(request): #list
    posts =Post.objects.all()
    paginator = Paginator(posts, 3) # 3 posts in each page
    page =request.GET.get ('page') #define page
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts= paginator.page (paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts,'page':page})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    