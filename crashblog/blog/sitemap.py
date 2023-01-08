from django.contrib.sitemaps import Sitemap
from .models import Category, Post 

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at