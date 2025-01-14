from django.urls import path
from .views import UserView
from .views import ChannelView
from .views import MessagesView
from .views import UserChannelView

urlpatterns = [
    path('users', UserView.as_view()),
    path('channels', ChannelView.as_view()),
    path('messages', MessagesView.as_view()),
    path('userChannel', UserChannelView.as_view())
]