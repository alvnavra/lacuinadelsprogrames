from django.contrib.sitemaps import Sitemap
from posts.models import Blog, Post

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
