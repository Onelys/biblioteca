from dataclasses import fields
from pyexpat import model
from . models import Autor
from django import forms

class AutorForm(forms.ModelForm):
   class Meta:
      model = Autor
      fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']