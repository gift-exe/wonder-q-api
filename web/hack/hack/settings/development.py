from .base import *




# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default':{
    'ENGINE':'django.db.backends.postgresql',
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'madvirus@madvirus.io'
# DOMAIN = os.getenv("DOMAIN")
# SITE_NAME = "hackkk"
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env("EMAIL_PORT")