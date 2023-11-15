from .views import *
from django.urls import path

#Urls de app Usuario
urlpatterns = [
    path("recompensa/", ListRecompensaView.as_view(), name='recompensa'),
    path("recompensa/agregar_recompensa/", NewRecompensa.as_view(), name='new_recompensa')    
]
