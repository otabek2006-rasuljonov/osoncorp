from .models import SiteSettings


def site_settings(request):
    settings = SiteSettings.load()
    return {'site_settings': settings}
