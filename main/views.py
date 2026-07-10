from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib import messages

from .models import Cliente
from .forms import CreateUserForm, ClienteForm
from .email import EnviarEmail

import string, random


def index(request):

    if request.method == 'GET':
        return render(request, "inicio.html")

def criar_cliente(request):
    
    if request.method == 'GET':
        user_form = CreateUserForm()
        cliente_form = ClienteForm(initial={'purl': ''})
        context = {'user_form': user_form, 'cliente_form': cliente_form}
        return render(request, "criar_cliente.html", context)
    elif request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        print(user_form.is_valid())
        print(cliente_form.is_valid())
        if user_form.is_valid() and cliente_form.is_valid():
            # Salva o usuário primeiro
            user = user_form.save()
           
            # Cria uma instancia do cliente sem salvar no banco de dados
            purl = criar_hash()
            cliente = cliente_form.save(commit=False)
            cliente.purl = purl

            # Associa o usuário ao cliente
            cliente.user = user

            # salva o cliente no banco de dados
            cliente.save();

            email = user_form.cleaned_data['email']
            print(email, purl)
            email_confirmacao = EnviarEmail()
            email_confirmacao.enviar_email_confirmacao_novo_cliente(email, purl)
            
            messages.success(request, 'Conta criada com sucesso')
            return redirect('index')
    
        context = {'user_form': user_form, 'cliente_form': cliente_form}
        return render(request, "criar_cliente.html", context)
        
def confirmar_email(request):
    if request.method == 'GET':

        # verificar se existe na query string um purl
        if request.GET.get('purl') == None:
            return redirect('index');

        purl = request.GET.get('purl')

        # verifica se purl é válido
        if len(purl) != 12:
            return redirect('index');
    
        # validar email
        try:
            cliente = Cliente.objects.get(purl=purl)
            cliente.purl = None
            cliente.ativo = True
            cliente.save()
            return render(request, 'conta_confirmada_sucesso.html')
        except Cliente.DoesNotExist:
            return redirect('index')

def login_cliente(request):
    
    if request.method == 'GET':
        return HttpResponse('Página Login')

def criar_hash(tamanho=12):
    # Define os caracteres permitidos (letras maiúsculas/minúsculas e números)
    caracteres = string.ascii_letters + string.digits
    
    # Gera a string aleatória de 12 caracteres
    purl = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return purl
        

