from .dev import *

STATIC_ROOT = '/var/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rahul',
        'USER': 'rahul',
        'PASSWORD': '3pQ#AYmu4+Yr7FnS',
        'HOST': 'rahul.ccsoekkpmuhy.us-west-2.rds.amazonaws.com',
        'PORT': '3306'
    }
}

