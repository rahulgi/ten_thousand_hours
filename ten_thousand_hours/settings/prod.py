from .dev import *

STATIC_ROOT = '/var/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's3player',
        'USER': 'mediaServer',
        'PASSWORD': 'D36utewRuSpA',
        'HOST': 'mauerbac-media-db.ccsoekkpmuhy.us-west-2.rds.amazonaws.com',
        'PORT': '3306'
    }
}

