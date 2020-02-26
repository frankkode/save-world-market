from django.urls import path
from . import views
from .views import (blog_news_index)




urlpatterns = [
    path("", views.blog_news_index, name="blog_news_index"),
    path("<int:pk>/", views.blog_news_detail, name="blog_news_detail"),
    path("<category>/", views.blog_news_category, name="blog_news_category"),
]