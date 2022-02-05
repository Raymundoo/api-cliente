import datetime
import json
import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from biblioteca.models import Libro,Autor
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from biblioteca.forms import LibroForm,AutorForm


def formulario_buscar(request): 
    return render(request, 'formulario_buscar.html') 
 
def buscar(request): 
    errors = [] 
    if 'q' in request.GET: 
        q = request.GET['q'] 
        if not q: 
           errors.append('Por favor introduce un termino de busqueda.') 
        elif len(q) > 20: 
          errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.') 
        else: 
          libros = Libro.objects.filter(titulo__icontains=q) 
          return render(request, 'resultados.html',{'libros': libros, 'query': q}) 
 
    return render(request, 'formulario_buscar.html', {'errors': errors})
# ----------------Class de Libro-----------------------------------------------
class LibrosList(ListView):
    model = Libro
    template_name='libros_list.html'

class LibroCreate(CreateView):
    model= Libro
    form_class=LibroForm
    template_name='libros_form.html'
    success_url=reverse_lazy('libro_lista')

class LibroUpdate(UpdateView):
    model = Libro
    form_class=LibroForm
    template_name='libros_form.html'
    success_url=reverse_lazy('libro_lista')

class LibroDelete(DeleteView):
    model = Libro
    template_name='libros_delete.html'
    success_url=reverse_lazy('libro_lista')

# ----------------Funciones de Libro-----------------------------------------------
def libro_list(request):
    libro=Libro.objects.all()
    datos = {'libro':libro,'func':'f'}
    return render(request,'libros_list.html',datos)

def libro_add(request):
    if request.method=='POST':
        form=LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_funct_lista')
    else:
        form=LibroForm()
    
    return render(request,'libros_form.html',{'form':form})


def libro_edit(request,id_libro):
    libro=Libro.objects.get(id=id_libro)
    if request.method=='GET':
        form = LibroForm(instance=libro)
    else:
        form=LibroForm(request.POST,instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_funct_lista')
    return render(request,'libros_form.html',{'form':form})

def libro_delete(request,id_libro):
    libro=Libro.objects.get(id=id_libro)
    if request.method=='POST':
        libro.delete()
        return redirect('libro_funct_lista')
    return render(request,'libros_delete.html',{'libro':libro,'def':'def'})

# ----------------Class de Autor-----------------------------------------------
class AutorList(ListView):
    model = Autor
    template_name='autor/autor_list.html'

class AutorCreate(CreateView):
    model= Autor
    form_class=AutorForm
    template_name='autor/autor_form.html'
    success_url=reverse_lazy('autor_lista')

class AutorUpdate(UpdateView):
    model = Autor
    form_class=AutorForm
    template_name='autor/autor_form.html'
    success_url=reverse_lazy('autor_lista')

class AutorDelete(DeleteView):
    model = Autor
    template_name='autor/autor_delete.html'
    success_url=reverse_lazy('autor_lista')
# ----------------Funct de Autor-----------------------------------------------
def autor_list(request):
    autor=Autor.objects.all()
    datos = {'autor':autor,'func':'f'}
    return render(request,'autor/autor_list.html',datos)

def autor_add(request):
    if request.method=='POST':
        form=AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_funct_lista')
    else:
        form=AutorForm()
    
    return render(request,'autor/autor_form.html',{'form':form})

def autor_edit(request,id_autor):
    autor=Autor.objects.get(id=id_autor)
    if request.method=='GET':
        form = AutorForm(instance=autor)
    else:
        form=AutorForm(request.POST,instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_funct_lista')
    return render(request,'autor/autor_form.html',{'form':form})

def autor_delete(request,id_autor):
    autor=Autor.objects.get(id=id_autor)
    if request.method=='POST':
        autor.delete()
        return redirect('autor_funct_lista')
    return render(request,'autor/autor_delete.html',{'autor':autor,'def':'def'})


# ----------------API de Autor-----------------------------------------------
def autor_lista_api(request):

    endpoint = "http://127.0.0.1:8000/api/autores/"
    response = requests.get(url=endpoint, timeout=5)
    object_list = []
    if response.status_code == 200:
        object_list = json.loads(response.content)

    datos = {'object_list': object_list}
    return render(request, 'autor/autor_list_api.html', datos)


def autor_add_api(request):

    if request.method=='POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            endpoint = "http://127.0.0.1:8000/api/autores/"
            response = requests.post(url=endpoint, data=data, timeout=5)
            print(response.status_code)
            if response.status_code == 201:
                print("OK")
                return redirect('autor_lista_api')
    else:
        form = AutorForm()
    
    return render(request, 'autor/autor_form.html',{'form': form})


def autor_edit_api(request, id_autor):

    endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
    response = requests.get(url=endpoint, timeout=5)
    if response.status_code == 200:
        autor_api = json.loads(response.content)
    else:
        return redirect('autor_lista_api')


    if request.method == 'GET':
        form = AutorForm(initial=autor_api)
    else:
        form = AutorForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            response = requests.put(url=endpoint, data=data, timeout=5)
            return redirect('autor_lista_api')
    return render(request,'autor/autor_form.html', {'form': form})


def autor_delete_api(request, id_autor):

    if request.method == 'POST':
        endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
        response = requests.delete(url=endpoint, timeout=5)
        if response.status_code == 204:
            print("OK")
            return redirect('autor_lista_api')
    else:
        endpoint = "http://127.0.0.1:8000/api/autores/{id_autor}/".format(id_autor=id_autor)
        response = requests.get(url=endpoint, timeout=5)
        if response.status_code == 200:
            autor = json.loads(response.content)
        else:
            return redirect('autor_lista_api')
    return render(request, 'autor/autor_delete.html', {'autor': autor})


def libro_lista_api(request):

    endpoint = "http://127.0.0.1:8000/api/libros/"
    response = requests.get(url=endpoint, timeout=5)
    object_list = []
    if response.status_code == 200:
        object_list = json.loads(response.content)

    datos = {'object_list': object_list}
    return render(request, 'libros_list_api.html', datos)


def libro_add_api(request):

    if request.method=='POST':
        form = LibroForm(request.POST)
        if form.is_valid():
          
            form.cleaned_data["editor"] = form.cleaned_data.get("editor").id
            form.cleaned_data["autores"] = list(form.cleaned_data.get("autores").values_list("id", flat=True))
            form.cleaned_data["fecha_publicacion"] = form.cleaned_data.get("fecha_publicacion").strftime("%Y-%m-%d")
            data = json.dumps(form.cleaned_data)
            endpoint = "http://127.0.0.1:8000/api/libros/"
            response = requests.post(url=endpoint, data=data, timeout=5)

            if response.status_code == 201:
                print("OK")
                return redirect('libro_lista_api')
    else:
        form = LibroForm()
    
    return render(request, 'libros_form.html', {'form': form})


def libro_edit_api(request, id_libro):

    endpoint = "http://127.0.0.1:8000/api/libros/{id_libro}/".format(id_libro=id_libro)
    response = requests.get(url=endpoint, timeout=5)
    if response.status_code == 200:
        libro_api = json.loads(response.content)
    else:
        return redirect('libro_lista_api')


    if request.method == 'GET':
        form = LibroForm(initial=libro_api)
    else:
        form = LibroForm(request.POST)
        if form.is_valid():
            form.cleaned_data["editor"] = form.cleaned_data.get("editor").id
            form.cleaned_data["autores"] = list(form.cleaned_data.get("autores").values_list("id", flat=True))
            form.cleaned_data["fecha_publicacion"] = form.cleaned_data.get("fecha_publicacion").strftime("%Y-%m-%d")
            data = json.dumps(form.cleaned_data)
            response = requests.put(url=endpoint, data=data, timeout=5)
            return redirect('libro_lista_api')

    return render(request, 'libros_form.html', {'form': form})


def libro_delete_api(request, id_libro):

    endpoint = "http://127.0.0.1:8000/api/libros/{id_libro}/".format(id_libro=id_libro)
    if request.method == 'POST':
        response = requests.delete(url=endpoint, timeout=5)
        if response.status_code == 204:
            print("OK")
            return redirect('libro_lista_api')
    else:        
        response = requests.get(url=endpoint, timeout=5)
        if response.status_code == 200:
            libro = json.loads(response.content)
        else:
            return redirect('libro_lista_api')
    return render(request, 'libros_delete.html', {'libro': libro})


