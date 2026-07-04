from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def index(request):

    if request.method == 'GET':
        return render(request, "inicio.html")

def criar_cliente(request):
    if request.method == 'GET':
        # form = ClienteForm()

        # context = {'form': form}

        return render(request, "criar_cliente.html")
    elif request.method == 'POST':
        # print(request.POST['text_email'])
        cliente = Cliente()
        cliente.nome_cliente = request.POST['text_nome_completo']
        cliente.morada = request.POST['text_morada']
        cliente.cidade = request.POST['text_cidade']
        cliente.telefone = request.POST['text_telefone']
        cliente.save()

        return render(request, "criar_cliente.html")
# def cadastrar_cliente(request):
