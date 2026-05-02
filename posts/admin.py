from django.contrib import admin
from .models import Category, Expert, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'title')
    raw_id_fields = ('user',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author', 'category', 'cover_image', 'is_published')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
    )
