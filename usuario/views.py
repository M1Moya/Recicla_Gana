from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import*

# Create your views here.
class ListRecompensaView(ListView):
    model = Canjeables
    template_name = "list_recompensa.html"

class NewRecompensa(CreateView):
    model = Canjeables
    template_name = "new_recompensa.html"
    fields = ["recompensa", "categoria", "puntos"]
    success_url = reverse_lazy("recompensa")
