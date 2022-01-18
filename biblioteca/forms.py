from django import forms
from biblioteca.models import Libro,Autor
class LibroForm(forms.ModelForm): 
    class Meta:
        model=Libro
        fields= [ 
            'titulo', 
            'autores',  
            'editor', 
            'fecha_publicacion',
        ]
        labels={
            'titulo':'Titulo', 
            'autores':'Autor',  
            'editor':'Editor', 
            'fecha_publicacion':'Fecha de Publicacion',
        }
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}), 
            'autores':forms.CheckboxSelectMultiple(),  
            'editor':forms.Select(attrs={'class':'form-control'}), 
            'fecha_publicacion':forms.TextInput(attrs={'class':'form-control'}),
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=[ 
            'nombre',
            'apellidos',
            'email',
        ]
        labels={
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'email':'Correo Electronico',
        }
        widget={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

