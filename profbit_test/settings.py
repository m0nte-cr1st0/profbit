import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'a5k$b*3_m79x!hn90=unwapw^rn)nb_fy9i06#d&eogoy$w+#t'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'order'
]

ROOT_URLCONF = 'profbit_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'context_processors.connection_to_db',
            ],
        },
    },
]

WSGI_APPLICATION = 'profbit_test.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'profbit_db',
        'USER': 'profbit_user',
        'PASSWORD': 'profbit_pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
