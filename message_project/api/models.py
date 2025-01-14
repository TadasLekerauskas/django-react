from django.db import models

# Create your models here.
# class for user entity
class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=30)

# class for channel
class Channel(models.Model):
    name = models.CharField(max_length=25)

# class for messages
class Messages(models.Model):
    text = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

# class for saving user-channel pairs to save who are inside the channel
class UserChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

