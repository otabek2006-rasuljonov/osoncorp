from django.shortcuts import render
from posts.models import Post, Category, Expert


def home(request):
    posts = Post.objects.filter(is_published=True).select_related('author', 'category', 'author__user').order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts})


def categories(request):
    cats = Category.objects.all().order_by('name')
    return render(request, 'core/categories.html', {'categories': cats})
