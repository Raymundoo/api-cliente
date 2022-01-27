#!
# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Models
from biblioteca.models import Autor, Libro

# Serializers
from biblioteca.serializers import AutorSerializer, LibroSerializer, LibroListaSerializer


@api_view(['GET', 'POST'])
def autor_list_api(request):
    """
    Listar todos los autores o agregar un nuevo autor usando una vista basada en funcion.
    """
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AutorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def autor_detail_api(request, pk):
    """
    Retrieve, update or delete a code autor.
    """
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AutorSerializer(autor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        autor.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def libro_list_api(request):
    """
    Listar todos los libros o agregar un nuevo libro.
    """
    if request.method == 'GET':
        libros = Libro.objects.select_related('editor').prefetch_related('autores').all()
        serializer = LibroListaSerializer(libros, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroListaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def libro_detail_api(request, pk):
    """
    Retrieve, update or delete a code libro.
    """
    try:
        libro = Libro.objects.select_related('editor').prefetch_related('autores').get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(libro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        libro.delete()
        return HttpResponse(status=204)