from django.urls import path
from . import consumers



websocket_urlpatterns=[
    path('ws/sc/<str:gname>/',consumers.MysyncConsumer.as_asgi()),
    path('ws/wsc/<str:gname>/',consumers.MyConsumer.as_asgi()),
]