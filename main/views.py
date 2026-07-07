from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib import messages

from .models import Cliente
from .forms import CreateUserForm, ClienteForm

# Create your views here.
def index(request):

    if request.method == 'GET':
        return render(request, "inicio.html")

def criar_cliente(request):
    
    if request.method == 'GET':
        form1 = CreateUserForm()
        form2 = ClienteForm()
        context = {'form1': form1, 'form2': form2}
        return render(request, "criar_cliente.html", context)
    elif request.method == 'POST':
        form1 = CreateUserForm(request.POST)
        form2 = ClienteForm(request.POST)
        print(form1.is_valid())
        print(form2.is_valid())
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.refresh_from_db()
            user.cliente.morada = form2.cleaned_data.get('morada')
            user.cliente.cidade = form2.cleaned_data.get('cidade')
            user.cliente.telefone = form2.cleaned_data.get('telefone')
            user.save();
            # raw_password = form1.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            # messages.success(request, 'Conta criada com sucesso')
            return redirect('index');
    
        context = {'form1': form1, 'form2': form2}
        return render(request, "criar_cliente.html", context)
        
        # cliente = Cliente()
        # cliente.nome_cliente = request.POST['text_nome_completo']
        # cliente.morada = request.POST['text_morada']
        # cliente.cidade = request.POST['text_cidade']
        # cliente.telefone = request.POST['text_telefone']
        # cliente.save()

        
# def cadastrar_cliente(request):
