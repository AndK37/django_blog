from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
import datetime

# Create your views here.
def index(request, page=0):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts[page * 5:(page + 1) * 5]})

def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            dj_login(request, user)
        return redirect('index')
    return render(request, 'blog/login.html', {})

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['login'], None, request.POST['password'])
        user.save()
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            dj_login(request, user)
        return redirect('index')
    return render(request, 'blog/register.html', {})

def logout(request):
    dj_logout(request)
    return redirect('index')

def post(request, post_id):
    if request.method == 'POST':
        comment = Comment.objects.create(post=get_object_or_404(Post, id=post_id), 
                                         user=User.objects.get(username=request.user.username), 
                                         text=request.POST['comment-text'])
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    return render(request, 'blog/post.html', {'post': post, 'comments': comments})

def create_post(request):
    if request.method == 'POST':
        post = Post.objects.create(title=request.POST['title'],
                            description = request.POST['desc'],
                            content=request.POST['content'])
        post.save()
        return redirect('index')
    return render(request, 'blog/create_post.html', {})

def update_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.filter(id=post_id).update(title=request.POST['title'],
                            description = request.POST['desc'],
                            content=request.POST['content'])
        return redirect('index', post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/update_post.html', {'post': post})
