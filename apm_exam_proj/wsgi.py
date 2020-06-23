"""
WSGI config for apm_exam_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apm_exam_proj.settings')
if os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apm_exam_proj.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apm_exam_proj.settings')
application = get_wsgi_application()
