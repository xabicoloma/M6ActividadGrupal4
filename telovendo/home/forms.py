from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa','nombre_solicitante','email','telefono','rubro_proveedor','direccion','comentario']
        labels = {'Nombre empresa':'nombre_empresa',
                'Nombre solicitante' : 'nombre_solicitante',
                'Correo' : 'email',
                'Telefono de contacto' :'telefono',
                'Rubro de proveedor' :'rubro_proveedor',
                'Dirección' : 'direccion',
                'Comentario' : 'comentario'
                }