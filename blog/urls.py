from django.conf import settings # Nos traemos los settings (el fichero de settings)
from django.conf.urls.static import static #Declaramos las rutas estáticas.


from django.contrib import admin
from filebrowser.sites import site
from django.urls import path, include
from django.conf.urls import url

from posts.views import index, blog, post, search, post_update, post_delete, post_create, categories

from django.conf.urls.i18n import i18n_patterns

from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
    'posts':PostSitemap
}

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/',  blog, name='post-list'),
    path('search/', search, name='search'),
    path('categories/<id>/', categories, name='categories'),
    path('create/',  post_create, name='post-create'),
    path('post/<id>/',  post, name='post-detail'),
    path('post/<id>/update/',  post_update, name='post-update'),
    path('post/<id>/delete/',  post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
