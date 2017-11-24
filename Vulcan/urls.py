from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', lambda x: HttpResponseRedirect('/upload/basic/')),
    url(r'^upload/', include('fileupload.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
 #   from django.conf.urls.static import static
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
