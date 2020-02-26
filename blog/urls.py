from django.urls import path
from django.conf import settings
from django.conf.urls.static import static






from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
#main urls
from . import views

urlpatterns = [
    path('', views.PostListView, name='blog-home'),
    path('user/<str:username>', views.UserPostListView, name='user-posts'),
    path('post/<int:id>/', views.PostDetailView, name='post-detail'),
    path('post/new/', views.PostCreateView, name='post-create'),
    path('post/<int:id>/update/', views.PostUpdateView, name='post-update'),
    path('post/<int:id>/delete/', views.PostDeleteView, name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('success/', views.Success, name='blog-success'),
    path('contact/', views.Contact, name='blog-contact'),
]





