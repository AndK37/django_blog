from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    # image = models.ImageField()
    content = models.TextField(blank=False, null=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date) + ' | ' + self.user.username + ' | ' + self.post.title