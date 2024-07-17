import os.path
import os
from pathlib import Path

import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-mx3@-!(-+=49-1kywr)xpnj(cw21i%bcz*69090vd8q%&^f_%v"

DEBUG = True

ALLOWED_HOSTS = ["*"]  # Choose one

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "active_link"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vidyasagar_student_mgmt.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "vidyasagar_student_mgmt.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vidyasagar_database',
        'USER': 'viydasagar_admin',
        'PASSWORD': 'vidya_admin_sagar#1921',
        'HOST': 'vidyasagar-database.c5iw8w0iyfy3.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT= '/static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'app.customuser'

AUTH_USER_MODEL = 'app.customuser'

AWS_ACCESS_KEY_ID = 'AKIAZI2LFR4KFYXVWUXY'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'vidyasagar-admin'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
