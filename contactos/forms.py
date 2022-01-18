from django import forms 
 
class FormularioContactos(forms.Form): 
     asunto = forms.CharField(max_length=100) 
     email = forms.EmailField(required=False,label='Tu correo electronico') 
     mensaje = forms.CharField(widget=forms.Textarea)
