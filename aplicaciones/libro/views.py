from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor

def inicio(request):
   return render(request, 'index.html')

def crearAutor(request):
   if request.method == 'POST':
      autor_form = AutorForm(request.POST)
      if autor_form.is_valid():
         autor_form.save()
         return redirect('inicio')
   else:
      autor_form = AutorForm()
      contexto ={
         'autor_form':autor_form
      }
      return render(request, 'libro/crear_autor.html', contexto)
   
def listarAutor(request):
   autores = Autor.objects.all()
   contexto = {
      'autores':autores
   }
   return render(request, 'libro/listar_autores.html', contexto)
