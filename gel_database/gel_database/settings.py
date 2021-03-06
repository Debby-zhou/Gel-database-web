"""
Django settings for gel_database project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f$o3mhfl(fm6d#vjxkg5tiag#!#g&0o=j#b3%xw533@v_(d00%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
ALLOWED_HOSTS = ['db','db.smagel.nchc.org.tw']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contents',
    'welcome',
    'experiment',
    'simulation',
    'analysis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gel_database.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["./template"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gel_database.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'experiment',
        'USER': 'experiment_user',
        'PASSWORD': 'experiment920344',
        'HOST': 'db',
        'PORT': '3306',        
    },
    'simulationdb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simulation',
        'USER': 'simulation_user',
        'PASSWORD': 'simulation920344',
        'HOST': 'db',
        'PORT': '3306',        
    },
    'analysisdb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'analysis',
        'USER': 'analysis_user',
        'PASSWORD': 'analysis920344',
        'HOST': 'db',
        'PORT': '3306',        
    }, 
    'userdb': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DATABASE_APPS_MAPPING = {
    'admin': 'default',
    'welcome': 'userdb',
    'contents': 'userdb',
    'simulation': 'simulationdb',
    'analysis': 'analysisdb',
    'experiment': 'default',
}
#DATABASE_ROUTERS = ['gel_database.db_router.simulationRouter','gel_database.db_router.analysisRouter']
CACHES = {
     "default": {
         "BACKEND": "django_redis.cache.RedisCache",
         "LOCATION": "redis://redis:6379/1",
         "OPTIONS": {
             "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "redisredis",
         },
     }
 }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
