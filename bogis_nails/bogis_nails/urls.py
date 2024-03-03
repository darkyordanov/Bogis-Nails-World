from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('bogis_nails.core.urls')),
    path('contacts/', include('bogis_nails.contacts.urls')),
    path('catalog/', include('bogis_nails.catalog.urls')),
    path('schedule/', include('bogis_nails.schedule.urls')),
    path('products/', include('bogis_nails.product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
