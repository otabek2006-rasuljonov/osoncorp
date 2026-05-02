from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('site_name',)
        }),
        ('Favicon', {
            'fields': ('favicon_image', 'favicon_url'),
            'description': 'Upload a favicon image OR enter a favicon URL. Image takes priority.',
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
