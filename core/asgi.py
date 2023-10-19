"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.urls import path
import home.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(
        home.routing.websocket_urlpatterns

    )
    # Just HTTP for now. (We can add other protocols later.)
})