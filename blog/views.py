from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        post = Post.objects.create(title=request.POST['title'],
                            description = request.POST['desc'],
                            content=request.POST['content'])
        post.save()
    return render(request, 'blog/create_post.html', {})

def update_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.filter(id=post_id).update(title=request.POST['title'],
                            description = request.POST['desc'],
                            content=request.POST['content'])
        return redirect('index', post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/update_post.html', {'post': post})
