from django.shortcuts import render
from rest_framework import generics
from .models import User
from .models import Channel
from .models import Messages
from .models import UserChannel
from .serializers import UserSerializer
from .serializers import ChannelSerializer
from .serializers import MessagesSerializer
from .serializers import UserChannelSerializer

# Create your views here.

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChannelView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class MessagesView(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

class UserChannelView(generics.ListAPIView):
    queryset = UserChannel.objects.all()
    serializer_class = UserChannelSerializer