from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = "cr8"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("models/", include("cr8.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
