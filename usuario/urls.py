from .views import *
from django.urls import path

#Urls de app Usuario
urlpatterns = [
    path("recompensa/", ListRecompensaView.as_view(), name='recompensa')
]
