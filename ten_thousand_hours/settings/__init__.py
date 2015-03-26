import os

if os.environ.get('ENV') == 'production':
    from .prod import *
else:
    from .dev import *
