"""
ASGI config for doctorspot project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctorspot.settings')

application = get_asgi_application()