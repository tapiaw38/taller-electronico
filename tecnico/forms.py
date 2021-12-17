from django import forms
from tecnico.models import Tecnico, Cliente


class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico

        fields = [

            'fecha',
            'cliente',
            'producto',
            'marca',
            'modelo',
            'color',
            'serie',
            'estado',
        ]

        labels = {

            'fecha':'Fecha de solicitud',
            'cliente':'Cliente',
            'producto':'Producto',
            'marca':'Marca',
            'modelo':'Modelo',
            'color':'Color',
            'serie':'N° de serie',
            'estado':'Estado del dispositivo al ingresar',
        }

        widgets = {

            'fecha': forms.SelectDateWidget(),
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'producto': forms.TextInput(attrs={'class':'form-control','placeholder':'Pc - Celular - Otro'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Textarea(attrs={'class': 'form-control','rows':3}),

        }

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Tecnico

        fields = [

            'entrega',
            'fechaen',
            'diagnostico',
            'realizar',
            'observacion',
            'precio',

        ]

        labels = {

            'entrega': 'Entrega del producto',
            'fechaen':'Fecha de entrega',
            'diagnostico':'Diagnostico',
            'realizar':'Proceso realizado',
            'observacion':'Observación',
            'precio':'Precio',

        }

        widgets = {
            'entrega': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'fechaen': forms.SelectDateWidget(),
            'diagnostico': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'realizar': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),


        }