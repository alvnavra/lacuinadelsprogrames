from django.conf import settings # Nos traemos los settings (el fichero de settings)
from django.conf.urls.static import static #Declaramos las rutas estáticas.


from django.contrib import admin
from filebrowser.sites import site
from django.urls import path, include

from posts.views import index, blog, post, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/',  blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>/',  post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)