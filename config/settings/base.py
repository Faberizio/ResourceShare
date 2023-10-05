from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
CUSTOM_APPS = [
    "apps.user",
    "apps.resources",
    "apps.core",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
]

INSTALLED_APPS = [*DEFAULT_APPS, *CUSTOM_APPS, *THIRD_PARTY_APPS]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.log.simple_logging_middleware",
    # "apps.core.middleware.logging.ViewExecutionTimeMiddleware",
    #"apps.core.middleware.logging.PrintingNewLineMiddleware",
]
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "templates")],
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR / "static")]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

LOGIN_URL = "login-view"

# Logger configuration
LOGGING = {
    'version': 1,  # dictConfig format version
    'loggers': {
        'logging_mw': {
            'handlers': ['file', 'console'],  # Include both console and file handlers
            'level': 'DEBUG',  # Define the log level for this logger
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # Corrected the class name
            "filters": ["only_if_debug_true"]  # Handle only if DEBUG=True
        },
        'file': {
            'level': 'INFO',
            # TODO: Search for more options for classes
            'class': 'logging.FileHandler',  # Corrected the class name
            'filename': str(BASE_DIR / "logs" / "req_res_logs.txt"),  # Specify the path to your log file
            "formatter": "verbose",
        },
    },
    'formatters': {
        "verbose": {
            # TODO: Search for more format log variables from official documentation
            "format": "{levelname} {asctime} {module} :: {message}",
            "style": "{",  # I want to use curly braces to access attributes
        },
    },
    'filters': {
        "only_if_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        # TODO: Call your own custom function to handle filter
    },
}
