import urllib.parse
from django.shortcuts import render
from .models import Category, Post, Comment

# Create your views here.
from blog_news.models import Post
from .forms import CommentForm
from django.contrib.auth.models import User


def blog_news_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, "blog_news_index.html", context)


def blog_news_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_news_category.html", context)


def blog_news_detail(request, pk):
    post = Post.objects.get(pk=pk)
    share_string = urllib.parse.quote(post.content)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "share_string": share_string,
    }

    return render(request, "blog_news_detail.html", context)


def blog_news_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_news_detail.html", context)