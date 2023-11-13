from django import forms
from .models import *

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material', 'valor_puntos']

