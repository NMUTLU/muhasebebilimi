from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from .models import Blog, Category  # database
from django.views.generic import ListView, DetailView  # post list and detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # sayfalama
from django.db.models import Q  # ara
from taggit.models import Tag  # tag
from django.template.defaultfilters import slugify  # slug
from blog import views
from django.http.request import QueryDict

# tagmixin


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

# kategori için


def get_refferer_urlparams(request):
    prev_params = request.META.get('HTTP_REFERER', '')
    if '?' in prev_params:
        prev_params = prev_params.split('?')[1]
    else:
        prev_params = ''
    query_dict = QueryDict(prev_params, mutable=True)
    return query_dict


def set_category(request, category):
    urlparams = get_refferer_urlparams(request)
    urlparams.pop('c', '')
    urlparams.update(c=category)
    return redirect('/?' + urlparams.urlencode())


# blog list ve detail index.html
class BlogPageView(TagMixin, ListView):
    allow_empty = True
    model = Blog
    template_name = 'index.html'
    paginate_by = 10
    make_object_list = True
    queryset = Blog.objects.all()
    ordering = ['-yayinlanma_tarihi']
    context_object_name = 'blog'
    # kategori için

    def get_queryset(self):
        posts = Blog.objects.order_by('-yayinlanma_tarihi')
        category = self.request.GET.get('c', '')
        if category:
            category_obj = Category.objects.get(name=category)
            posts = posts.filter(category=category_obj)
        return posts


class BlogDetailView(TagMixin, DetailView):
    template_name = 'post.html'
    model = Blog
    context_object_name = 'blog'


class SearchResultsView(TagMixin, ListView):
    model = Blog
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
<<<<<<< HEAD
        if query:
            object_list = Blog.objects.filter(
                Q(konu__icontains=query) |
                Q(alt_konu__icontains=query) |
                Q(metin__icontains=query)

            )
        else:
            object_list = self.model.objects.none()
=======
        object_list = Blog.objects.filter(
            Q(konu__icontains=query) |
            Q(metin__icontains=query)
        )
>>>>>>> b66558ea37ed9c66bab50d97cba846e6793daaa9
        return object_list

# taggit


class TagListView (TagMixin, ListView):
    template_name = 'index.html'
    model = Blog
    paginate_by = '10'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get('slug'))

# static templates


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "statik_temp/about.html")


def reklam(request):
    return render(request, "statik_temp/reklam.html")


def kaynaklar(request):
    return render(request, "statik_temp/kaynaklar.html")


def uyarı(request):
    return render(request, "statik_temp/uyarı.html")
