import requests
from django.shortcuts import render,redirect
def get_pokemon(request):
     url='https://pokeapi.co/api/v2/pokemon/?limit='
     errors = []
     
     if 'cant' in request.GET:
            cant=request.GET['cant']
            try:
                if int(cant) <= 0:
                    errors.append('ingresa un numero mayor a 0')
                    return render(request,'index.html',{'errors':errors})
                url+=cant
                response=requests.get(url)
                if response.status_code==200:
                    payload=response.json()
                    results=payload.get('results',[])
                    if results:
                        lista2 = []
                        dir={}
                        for pokemon in results:
                            nombre=pokemon['name']
                            response=requests.get(pokemon['url'])
                            if response.status_code==200:
                                payload=response.json()
                                img=payload.get('sprites',[])
                                id_pokemon=payload.get('id',[])
                                imgen=img['front_default']
                                dir={'nombre':nombre,'url_img':imgen,'id':id_pokemon}
                                lista2.append(dir)
                return render(request,'index.html',{'datos':lista2,'errors':errors})
            except ValueError:
                 if not cant: 
                     errors.append('Por favor introduce un numero.')
                 else:
                    errors.append('Por favor introduce un numero correcto')
     
     return render(request, 'index.html', {'errors':errors})
        


         
def info_pokemon(request,id_pokemon):
    arg=id_pokemon
    url='https://pokeapi.co/api/v2/pokemon/'
    url+=arg
    response=requests.get(url)
    
    if response.status_code==200:
        lista_datos = []
        
        payload=response.json()


        name=payload.get('name',[])
        peso=payload.get('weight',[])
        altura=payload.get('height',[])

        img=payload.get('sprites',[])
        imgen=img['front_default']

        habi=payload.get('abilities',[])

        movi=payload.get('moves',[])

        types=payload.get('types',[])
        if types:
            lista_tipos = []
            dir_tipos={}
            for tipo in types:
                tip=tipo['type']
                nombre=tip['name']
                response=requests.get(tip['url'])
                if response.status_code==200:
                    payload=response.json()
                    id_tip=payload.get('id',[])
                    dir_tipos={'nombre':nombre,'id_tip':id_tip}
                    lista_tipos.append(dir_tipos)
                
      
        datos={'name':name,'peso':peso,'altura':altura,'img':imgen}
        lista_datos.append(datos)
        tipos={'tipo':types}
    return render(request,'info_pokemon.html',{'datos':lista_datos,'tipo':lista_tipos,'habilidad':habi,'movimientos':movi})

def tipo_pokemon(request,id_tipo):
    arg=id_tipo
    url='https://pokeapi.co/api/v2/type/'
    url+=arg
    response=requests.get(url)
    if response.status_code==200:
        payload=response.json()
        tipo_pokemon=payload.get('pokemon',[])
        title=payload.get('name',[])
        print title
        if tipo_pokemon:
            lista = []
            dir={}
            for pokemon in tipo_pokemon:
                pok=pokemon['pokemon']
                nombre=pok['name']
                response=requests.get(pok['url'])
                if response.status_code==200:
                    payload=response.json()
                    img=payload.get('sprites',[])
                    id_pokemon=payload.get('id',[])
                    imgen=img['front_default']
                    dir={'nombre':nombre,'url_img':imgen,'id':id_pokemon}
                    lista.append(dir)
        return render(request,'index.html',{'tipo':'tipo','datos':lista,'title':title} )