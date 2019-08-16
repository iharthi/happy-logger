from django.urls import path

from entry.views import ReceiveMessageView

urlpatterns = [
    path('', ReceiveMessageView.as_view(), name='receive-message'),
]
