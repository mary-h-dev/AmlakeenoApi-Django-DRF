



ALLOWED_HOSTS = ["localhost",
                  "127.0.0.1",
                    "http://localhost:3000/",
                      "http://127.0.0.1:5173/",
                      "http://amlakeeno.ir",
                      "https://www.amlakeeno.ir",
                      "https://amlakeeno.ir",
                      "https://api.amlakeeno.ir",
                      "http://api.amlakeeno.ir",
                       "https://www.api.amlakeeno.ir",]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "origin",
    "dnt",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]


CORS_ALLOWED_ORIGIN_REGEXES = ["https://localhost:3000/"]
from corsheaders.defaults import default_methods

CORS_ALLOW_METHODS = (
    *default_methods,
    "POKE",
)


from pathlib import Path
import os

if os.name == "nt":
    VENV_BASE = os.environ["VIRTUAL_ENV"]
    os.environ["PATH"] = (
        os.path.join(VENV_BASE, "Lib\\site-packages\\osgeo") + ";" + os.environ["PATH"]
    )
    os.environ["PROJ_LIB"] = (
        os.path.join(VENV_BASE, "Lib\\site-packages\\osgeo\\data\\proj")
        + ";"
        + os.environ["PATH"]
    )


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&9#)f3m0li0drvya*(cun_%susb&1@0dddqa*p7gc^%z8pqt+e"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # installed package
    "django.contrib.gis",
    'jalali_date',
    "rest_framework",
    "rest_framework_gis",
    "corsheaders",
    "rest_framework.authtoken",
    "djoser",
    # installed app
    "listings.apps.ListingsConfig",
    "users.apps.UsersConfig",
    "posts.apps.PostsConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases




# DATABASES = {
#     "default": {
#         "ENGINE": "django.contrib.gis.db.backends.postgis",
#         "NAME": "amlak_db",
#         "USER": "postgres",
#         "PASSWORD": "Einesheikh1367",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }




DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "root",
        "PASSWORD": "VTpjiIDgC23613wQHNm1ConP",
        "HOST": "post-db",
        "PORT": "5432",
    }
}






# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_L10N = True
USE_TZ = True
# language
LANGUAGE_CODE = 'fa'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# stting by developer############################
AUTH_USER_MODEL = "users.User"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}

DJOSER = {
    # 'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,
    # 'SERIALIZERS': {},
    "USER_CREATE_PASSWORD_RETYPE": True,
    # 'ACTIVATION_URL': '#/activate/{uid}/{token}',
    # "SEND_ACTIVATION_EMAIL": True,
}


# email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

