from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from .consummers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]
