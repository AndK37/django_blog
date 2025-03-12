from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    # image = models.ImageField()
    content = models.TextField(blank=False, null=False)
    date = models.DateField(default=date.today)
