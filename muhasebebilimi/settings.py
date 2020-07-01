"""
Django settings for muhasebebilimi project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qp1ii!52m(!5mho=^&85)+mgw)fs9773j30_j+lfh87$mby^e('
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #site güvenliği için yayına alındığında false
SESSION_COOKIE_HTTPONLY            =   False
ADMIN_ENABLED  = False#site güvenliği için yayına alındığında false allowed_hosts="muhasebebilimi.com"
ALLOWED_HOSTS = ['*']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #yönlendirmeler uygulaması seo
    'django.contrib.sites',
    'django.contrib.redirects',
    
    #kendi uygulamalarımız# 
    'contact.apps.ContactConfig',
	'blog',
    #3. parti uygulamalar
    'ckeditor',
    'ckeditor_uploader',
    'django_cleanup',
    'crispy_forms',
    'widget_tweaks',
    ##tag
    'taggit',
    ##tag
    ## BEGİN Sitemap
    'django.contrib.sitemaps',
    ## END Sitemap
    #image optimisazyonu yeniden boyut
    'imagekit',

]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #yönlendirmeler uygulaması seo
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]
ROOT_URLCONF = 'muhasebebilimi.urls'   

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            ##context processor    
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'blog.context_processor.sidebar_context',
            ],
        },
    },
]
WSGI_APPLICATION = 'muhasebebilimi.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#crispy form
CRISPY_TEMPLATE_PACK = 'bootstrap4'
#ck editör
#CKEDITOR_CONFIGS = {
#    "default": {
#        "removePlugins": "stylesheetparser",
#        "allowedContent" : True,
#        "width" : "100%",        
#    }
#}
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
##sitemaps için bir site nesneyi veritabanından(kimliğiyle=1)bu ayarlar dosyasına ilişkilendirir. seo
SITE_ID = 1