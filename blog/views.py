from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    post = Post.objects.get(id=1)
    return render(request, 'blog/index.html', {'post': post})