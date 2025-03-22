from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:page>/', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('create/post/', views.create_post, name='create_post'),
    path('update/post/<int:post_id>', views.update_post, name='update_post'),
    path('delete/post/<int:post_id>', views.delete_post, name='delete_post'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]