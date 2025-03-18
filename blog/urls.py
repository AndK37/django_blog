from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('create/post/', views.create_post, name='create_post'),
    path('update/post/<int:post_id>', views.update_post, name='update_post'),
    path('login/', views.login, name='login'),
]