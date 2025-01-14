from rest_framework import serializers
from .models import User
from .models import Messages
from .models import Channel
from .models import UserChannel

# serialize for user entity
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

# serialize for user entity
class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'text', 'time', 'channel')

# serialize for user entity
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')

# serialize for user entity
class UserChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user', 'channel')
