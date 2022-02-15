"""
WSGI config for GeoLama project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["django_settings_module"]
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoLama.settings')
application = get_wsgi_application()
