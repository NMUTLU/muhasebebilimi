from django.contrib import admin
from .models import Blog, Category
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["konu", "alt_konu", "yayinlanma_tarihi", ]
    prepopulated_fields = {'slug': ('konu',)}
    list_display_links = ["konu", "yayinlanma_tarihi"]
    search_fields = ["konu"]
    list_filter = ["yayinlanma_tarihi"]

    class Meta:
        model = Blog


admin.site.register(Category)
