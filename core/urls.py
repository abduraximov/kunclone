from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.posts import urls

from .schema import swagger_urlpatterns

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(urls))
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
