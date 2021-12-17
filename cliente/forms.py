from django import forms
from cliente.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [

            'nombre',
            'dni',
            'direccion',
            'correo',
            'telefono',
        ]

        labels = {

            'nombre':'Nombre y Apellido',
            'dni':'D.N.I.',
            'direccion':'Dirección',
            'correo':'Email',
            'telefono':'Teléfono',
        }

        widgets = {

            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),

        }