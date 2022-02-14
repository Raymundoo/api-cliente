# -*- coding: utf-8 -*-
import json
import requests
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from api.models import RaynhardtJWT
from prueba import settings


def create_token_api_raynhardt():
    endpoint = "http://raynhardtapi.net:8000/api/token/"
    data = {"username": settings.API_USER, "password": settings.API_PASSWORD}
    response = requests.post(url=endpoint, data=data, timeout=5)

    if response.status_code == 200:
        jwt = RaynhardtJWT.objects.create(
            access_token=json.loads(response.content).get("access"),
            refresh_token=json.loads(response.content).get("refresh"),
        )
        return jwt
    else:
        return response.status_code


def refresh_token_api_raynhardt():
    datos_api = RaynhardtJWT.objects.all().first()

    endpoint = "http://raynhardtapi.net:8000/api/token/refresh/"
    data = {"refresh": datos_api.refresh_token}
    response = requests.post(url=endpoint, data=data, timeout=5)
    # print(response.status_code)

    if response.status_code == 200:
        datos_api.access_token = json.loads(response.content).get("access")
        datos_api.save()
        return datos_api.access_token

    elif response.status_code == 401:  # El refresh ha expirado
        code = json.loads(response.content).get("code")
        if code == "token_not_valid":
            endpoint = "http://raynhardtapi.net:8000/api/token/"
            data = {"username": settings.API_USER, "password": settings.API_PASSWORD}
            response = requests.post(url=endpoint, data=data, timeout=5)
            if response.status_code == 200:
                datos_api.refresh_token = json.loads(response.content).get("refresh")
                datos_api.access_token = json.loads(response.content).get("access")
                datos_api.save()

        return response.status_code


def mr_olympia_lista_api(request):
    datos_api = RaynhardtJWT.objects.get(id=1)
    endpoint = "http://raynhardtapi.net:8000/v1/mrolimpya/"
    data = {"refresh": datos_api.refresh_token}
    acces_token = "Bearer {0}".format(datos_api.access_token)
    headers = {"Authorization": acces_token}
    response = requests.get(url=endpoint, headers={"Authorization": acces_token}, timeout=5)
    object_list = []

    if response.status_code == 200:
        object_list = json.loads(response.content).get("results")

    elif response.status_code == 401:  # El access token ha expirado
        message = json.loads(response.content).get("messages")[0].get("message")
        if message == "Token is invalid or expired":
            refresh_token_api_raynhardt()
            return redirect('mr_olympia_lista_api')

    datos = {'object_list': object_list, 'status_code': response.status_code}
    return render(request, 'olympia_list.html', datos)


def mascota_lista_api(request):

    datos_api = RaynhardtJWT.objects.all().first()
    if datos_api is None:
        datos_api = create_token_api_raynhardt()

    endpoint = "http://raynhardtapi.net:8000/v1/mascota/"
    data = {"refresh": datos_api.refresh_token}
    acces_token = "Bearer {0}".format(datos_api.access_token)
    headers = {"Authorization": acces_token}
    response = requests.get(url=endpoint, headers={"Authorization": acces_token}, timeout=5)
    object_list = []
    titulo = "Mascotas JWT"
    if response.status_code == 200:
        object_list = json.loads(response.content).get("results")

    elif response.status_code == 401:  # El access token ha expirado
        message = json.loads(response.content).get("messages")[0].get("message")
        if message == "Token is invalid or expired":
            refresh_token_api_raynhardt()
            return redirect('mascota_lista_api')

    datos = {'object_list': object_list, 'status_code': response.status_code}
    return render(request, 'mascotas_list.html', datos)


def mascota_lista_api_token(request):


    endpoint = "http://apitokenauthentication.net:8000/v1/mascota/"
    acces_token = "Token {0}".format(settings.TOKEN_AUTHENTICATION)
    headers = {"Authorization": acces_token}
    response = requests.get(url=endpoint, headers={"Authorization": acces_token}, timeout=5)
    object_list = []
    titulo = "Mascotas Token Authentication"
    if response.status_code == 200:
        print(response.content)
        object_list = json.loads(response.content)

     
    datos = {'object_list': object_list, 'status_code': response.status_code, 'titulo': titulo}
    return render(request, 'mascotas_list.html', datos)