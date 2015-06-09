from .dev import *

STATIC_ROOT = '/var/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rahul',
        'USER': 'rahul',
        'PASSWORD': 'test',
        'HOST': 'rahul.ccsoekkpmuhy.us-west-2.rds.amazonaws.com',
        'PORT': '3306'
    }
}

