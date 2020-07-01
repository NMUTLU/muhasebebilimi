from blog.models import Category
def sidebar_context(request):
    return {
        'categories': get_categories(request),
    }
def get_categories(request):
    return [c for c in Category.objects.all()]