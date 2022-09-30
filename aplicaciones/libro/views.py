from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
   autores = Autor.objects.filter(estado = True)
   contexto = {
      'autores':autores
   }
   return render(request, 'libro/listar_autores.html', contexto)

def editarAutor(request, id):
   autor_form = None
   error = None
   try:
      autor = Autor.objects.get(id = id)
      if request.method == 'GET':
         autor_form = AutorForm(instance = autor)
      else:
         autor_form = AutorForm(request.POST, instance = autor)
         if autor_form.is_valid():
            autor_form.save()
         return redirect('inicio')
   except ObjectDoesNotExist as e:
      error = e
      
   contexto = {
      'autor_form':autor_form,
      'error':error
   }
   return render(request, 'libro/crear_autor.html', contexto)

def eliminarAutor(request, id):
   autor = Autor.objects.get(id = id)
   if request.method == 'POST':
      autor.delete()
      return redirect('libro:listar_autores')
   contexto ={
      'autor':autor
      }
   return render(request,'libro/eliminar_autor.html', contexto)

def esconderAutor(request, id):
   autor = Autor.objects.get(id = id)
   if request.method == 'POST':
      autor.estado = False
      autor.save()
      return redirect('libro:listar_autores')
   contexto ={
      'autor':autor
      }
   return render(request,'libro/eliminar_autor.html', contexto)
      
      
       
