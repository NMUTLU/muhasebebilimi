from django.urls import path
from django.contrib import admin
from .views import BlogPageView,BlogDetailView,SearchResultsView,TagListView, set_category
from django.views.generic.base import TemplateView
from blog import views
##rss
from .feeds import LatestPostsFeed
##rss
##sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
##sitemaps
sitemaps = {
    "posts": PostSitemap,
}
##sitemaps
urlpatterns = [
    path('', BlogPageView.as_view(), name="index" ),
    path('<slug:slug>',BlogDetailView.as_view(), name="blog"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<str:slug>/',TagListView.as_view(), name='tagged'),
    #widget categori
    path('ac/<category>', set_category, name='set_cat'),
    #static web page
    path('about/',views.about,name = "about"),
    path('reklam/',views.reklam,name = "reklam"),
    path('kaynaklar/',views.kaynaklar,name = "kaynaklar"),
    path('uyarı/',views.uyarı,name = "uyarı"),
    ##rss
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    ##sitemaps
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    ]
