from rest_framework.schemas import get_schema_view

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

schema_view = get_schema_view(title='Risks API')


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path(r'', include(('britecorehiringtest.risks.urls', 'risks'), namespace='risks')),
    path(r'schema/', schema_view),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
