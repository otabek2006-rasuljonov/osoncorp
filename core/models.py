from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default='Osoncorp')
    favicon_image = models.ImageField(upload_to='favicon/', blank=True, null=True)
    favicon_url = models.URLField(blank=True, null=True, help_text='Favicon URL (if no image uploaded)')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

    def get_favicon(self):
        if self.favicon_image:
            return self.favicon_image.url
        if self.favicon_url:
            return self.favicon_url
        return None

    def save(self, *args, **kwargs):
        # Ensure only one instance exists (singleton)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
