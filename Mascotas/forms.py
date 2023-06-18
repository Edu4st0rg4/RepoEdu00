from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto                #nombre de la clase
        fields = ['codigo', 'marca', 'tipo', 'categoria','imagen'] #atributos de la clase
        labels = {                     #etiquetas asociadas a los atributos
            'codigo': 'Codigo',
            'marca' : 'Marca',
            'tipo' : 'Tipo',
            'categoria': 'Categoria',
            'imagen':'Imagen'
        }
        widgets = {
            'codigo' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese codigo..',
                    'id':'codigo',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese marca..',
                    'id':'marca',
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese tipo..',
                    'id':'tipo',
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }#cierre de widgets

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','password1','password2']