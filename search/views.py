from django.shortcuts import render
from blog.models import Post

# do search.
def do_search(request):
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "blog/home.html", {"posts": posts})
