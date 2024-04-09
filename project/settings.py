"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from configurations import Configuration, values


class Dev(Configuration):

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Imports secret values from .env file in main directory.
    DOTENV = BASE_DIR / '.env'

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()
    #'django-insecure-0r#db4pz99+st9-*#*qnsb-mpw9xhcuz9q@i@#iik$&$(uzsz1'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    # List ALLOWED_HOSTS in environment var named DJANGO_ALLOWED_HOSTS
    # "www.example.com,www.demo.com,www.whatever.org"
    ALLOWED_HOSTS = values.ListValue([])


    # Application definition

    INSTALLED_APPS = [
        'debug_toolbar',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'webpack_boilerplate',
        'crispy_forms',
        'crispy_bulma',
        'project_admin.apps.ProjectAdminConfig'
        ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'project.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
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

    WSGI_APPLICATION = 'project.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/5.0/ref/settings/#databases
    # Add DJANGO_DATABASE_URL to environment variables in production.

    DATABASES = values.DatabaseURLValue(
        f'sqlite:///{BASE_DIR}/db.sqlite3', environ_prefix='DJANGO'
    )


    # Password validation
    # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/5.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/

    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
            BASE_DIR / 'frontend/build',
            BASE_DIR / 'static',
    ]

    STATICFILES_STORAGES = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

    STATIC_ROOT = BASE_DIR / 'static_prod_test'

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # python-webpack-boilerplate Manifest File location.
    # https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_django/

    WEBPACK_LOADER = {
            'MANIFEST_FILE': BASE_DIR / 'frontend/build/manifest.json',
    }

    # Django Debug Toolbar
    INTERNAL_IPS = ['127.0.0.1']

    # Crispy Forms
    CRISPY_ALLOWED_TEMPLATE_PACKS = ('bulma',)
    CRISPY_TEMPLATE_PACK = 'bulma'

class Prod(Dev):
    DEBUG = False