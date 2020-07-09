from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    def items(self):
        return Blog.objects.all()#return Entry.objects.filter(is_draft=False)
    def lastmod(self, obj): 
        return obj.yayinlanma_tarihi
