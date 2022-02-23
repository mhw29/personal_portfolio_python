from turtle import pos
from django.shortcuts import render
from blog.models import Post, Comment
from django.db.models import Count
from .forms import CommentForm
# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on').annotate(num_comments=Count('comment'))
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.annotate(num_comments=Count('comment')).get(pk=pk)
    posts =     posts = Post.objects.order_by(
            '-created_on'
        )
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
        "posts": posts,
    }

    return render(request, "blog_detail.html", context)