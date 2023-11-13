from django.shortcuts import render
from django.views.generic import ListView, TemplateView, UpdateView
from .models import*

# Create your views here.
class ListRecompensaView(ListView):
    model = Canjeables
    template_name = "list_recompensa.html"
    context_object_name = "canjeable"
