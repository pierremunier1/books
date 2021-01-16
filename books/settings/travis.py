from . import *

import os 


if 'TRAVIS' in os.environ:

    SECRET_KEY = "ma)tgt4@)ffhujtexv87u65)%k5oqtt$&yn99e=p$_&fl!ryti"

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        },
    }