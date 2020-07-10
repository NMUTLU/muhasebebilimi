from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
<<<<<<< HEAD
=======
# IMAGE MEDIUM START
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
# IMAGE MEDIUM END
>>>>>>> b66558ea37ed9c66bab50d97cba846e6793daaa9

# kategori


class Category(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name

# vt


class Blog(models.Model):
    objects = models.Manager()      # varsayılan model yöneticisi
    konu = models.CharField(max_length=90, verbose_name="Başlık")
<<<<<<< HEAD
    altkonu_image = models.ImageField(upload_to='images/altkonu/', null = True, blank = True, verbose_name="alt başlık Fotoğraf Ekleyin", height_field = None, width_field = None, max_length = 100,)#resim olmasa bile ekleme yapar
=======
    altkonu_image = models.ImageField(upload_to='images/altkonu/', null=True, blank=True, verbose_name="alt başlık Fotoğraf Ekleyin",
                                      height_field=None, width_field=None, max_length=100,)  # resim olmasa bile ekleme yapar
    image_medium = ImageSpecField(source='altkonu_image', processors=[
                                  ResizeToFill(200, 100)], format='JPEG', options={'quality': 60})
>>>>>>> b66558ea37ed9c66bab50d97cba846e6793daaa9
    slug = models.SlugField(max_length=90, unique=True, null=False)
    # giriş olmasa bile ekleme yapar
    alt_konu = models.CharField(
        max_length=150, verbose_name="Alt_Başlık", null=True, blank=True,)
    metin = RichTextUploadingField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    yayinlanma_tarihi = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    # duzenleme tarihi ekle
    yazar = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar", null=True, blank=True,)
    # düzelmek için bak

    def get_unique_slug(self):
        slug = slugify(self.konu.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
            return unique_slug

    class Meta:
        ordering = ['-yayinlanma_tarihi']  # yayınlanma tarihine göre sırala

    def __str__(self):  # admin eklediğimiz postların başlığı neyse bize onu gösterecek
        return self.konu

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})
