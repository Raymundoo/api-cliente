from django.core.mail import send_mail 
from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from contactos.forms import FormularioContactos
 
def contactos(request): 
    if request.method == 'POST': 
        form = FormularioContactos(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            send_mail( 
                cd['asunto'], 
                cd['mensaje'], 
                cd.get('email', 'noreply@example.com'), 
                    ['siteowner@example.com'], 
             ) 
            return HttpResponseRedirect('/contactos/gracias/') 
    else: 
        form = FormularioContactos(initial={'asunto': 'Adoro tu sitio!!!'}) 
    return render(request, 'formulario-contactos.html', {'form': form}) 