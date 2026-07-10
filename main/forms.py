from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class ClienteForm(ModelForm):
    
    morada = forms.CharField(
        label="Endereço",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}),
    )
    cidade = forms.CharField(
        label="Cidade",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}),
    )

    telefone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefone'}),
    )

    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ['morada', 'cidade', 'telefone', 'purl']
        # exclude = ['user']

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repetir Senha'}),
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }),
            'password2': forms.PasswordInput(render_value = True, attrs={
                'class': 'form-control',
                'placeholder': 'Repetir Senha'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome Completo'
            })
        }
