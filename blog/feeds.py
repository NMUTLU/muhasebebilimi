from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Blog
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "Muhasebe Bil Makaleler"
    link = ""
    description = "Yeni makaleler Muhasebe Bilgisi."
    def items(self):
        #return Blog.objects.filter(status="Published")
        return Blog.objects.all().order_by("-yayinlanma_tarihi")[:5]
    def item_title(self, item):
        return item.konu

    def item_description(self, item):
        return truncatewords(item.metin, 30)


        
        
