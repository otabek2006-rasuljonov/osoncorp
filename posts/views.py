from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    category_slug = request.GET.get('category')
    posts = Post.objects.filter(is_published=True).select_related('author', 'category', 'author__user')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=selected_category)
    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'selected_category': selected_category,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'posts/post_detail.html', {'post': post})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, is_published=True).select_related('author', 'author__user')
    return render(request, 'posts/category_detail.html', {
        'category': category,
        'posts': posts,
    })
