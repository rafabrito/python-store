from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import *
from .forms import CreateUserForm, ClienteForm
from .email import EnviarEmail

import string, random


def index(request):

    if request.method == 'GET':
        return render(request, "inicio.html")

def loja(request):

    if request.method == 'GET':
        # buscar da lista de produtos disponíveis
        lista_produtos = None
        if request.GET.get('c') != None:
            if request.GET.get('c') != 'todos':
                c = request.GET.get('c')
                lista_produtos = Produto.objects.filter(visivel=True, deleted_at=None, categoria=c)
            else:
                lista_produtos = Produto.objects.filter(visivel=True, deleted_at=None)
        else:
            lista_produtos = Produto.objects.filter(visivel=True, deleted_at=None)

        # obtém a lista de categorias na forma de array através do flat=True
        lista_categorias = Produto.objects.values_list('categoria', flat=True).distinct()

        context = {
            'produtos': lista_produtos, 
            'categorias': lista_categorias
        }

        return render(request, "loja.html", context)

def adicionar_carrinho(request):

    if request.method == 'GET':
        # vai buscar pelo id_produto à query string
        if request.GET.get('id_produto') == None:
            return HttpResponse(len(request.session.get('carrinho'))) if request.session.get('carrinho') else HttpResponse('')

        # define o id do produto
        id_produto = request.GET.get('id_produto')

        produto = Produto.objects.filter(id=id_produto, visivel=True, stock__gt=1, deleted_at=None)
        resultados = True if len(produto) else False

        if resultados == False:
            return HttpResponse(len(request.session.get('carrinho'))) if request.session.get('carrinho') else HttpResponse('')

        # adiciona/gestão da variável de SESSAO do carrinho
        carrinho = {}

        if request.session.get('carrinho'):
            carrinho = request.session['carrinho']

        # adicionar o produto ao carrinho
        if id_produto in carrinho:
            #  já existe o produto. Acrescenta mais uma unidade
            carrinho[id_produto] += 1
        else:
            # adicionar novo produto ao carrinho
            carrinho[id_produto] = 1

        # atualiza os dados do carrinho na sessão
        request.session['carrinho'] = carrinho

        # devolve a resposta (número de produtos do carrinho)
        total_produto = 0
        for chave in carrinho:
            total_produto += carrinho[chave]
        
        return HttpResponse(total_produto)

def limpar_carrinho(request):

    if request.method == 'GET':
        # remover a variável da sessão e evita erro caso não exita a chave
        request.session.pop('carrinho', None)

    return render(request, "carrinho.html")

def carrinho(request):

    if request.method == 'GET':
        if request.session.get('carrinho') == None:
            context = {
                'carrinho': None
            }
        else:
            ids = []
            for id_produto in request.session.get('carrinho'):
                ids.append(id_produto)

            # obtém os produtos a partir de um array de ids
            resultados = Produto.objects.filter(id__in=ids)

            context = {
                'carrinho': request.session.get('carrinho')
            }

        print(resultados)
        return render(request, "carrinho.html", context)

def criar_cliente(request):
    
    if request.method == 'GET':
        # verifica se já existe sessão aberda
        if request.user.is_authenticated:
            return redirect('index')

        # cria os campos do form para o usuário/cliente
        user_form = CreateUserForm()
        cliente_form = ClienteForm(initial={'purl': ''})

        context = {'user_form': user_form, 'cliente_form': cliente_form}
        return render(request, "criar_cliente.html", context)

    elif request.method == 'POST':
        #  obtém os dados do form do usuário/cliente
        user_form = CreateUserForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        
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
           
            email_confirmacao = EnviarEmail()
            email_confirmacao.enviar_email_confirmacao_novo_cliente(email, purl)
            
            return render(request, "criar_cliente_sucesso.html")
    
        context = {'user_form': user_form, 'cliente_form': cliente_form}
        return render(request, "criar_cliente.html", context)
        
def confirmar_email(request):

    if request.method == 'GET':
        # verifica se já existe sessão aberda
        if request.user.is_authenticated:
            return redirect('index')
        
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

    context = {}
    if request.method == 'GET':
        # verifica se já existe um utilizador logado
        if request.user.is_authenticated:
            return redirect('index')
        
        return render(request, 'login_form.html', context)
    elif request.method == 'POST':
        usuario = request.POST.get('text_usuario')
        senha = request.POST.get('text_senha')
        # User = get_user_model()
        try:
            # cliente = Cliente.objects.get(user__email=usuario, ativo=1, purl=None)
            cliente = Cliente.objects.get(user__username=usuario, ativo=1, purl=None)
            print(cliente)
            if cliente:
                user = authenticate(request, username=usuario, password=senha)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Login inválido')
                    return render(request, 'login_form.html', context)
        except Cliente.DoesNotExist:
            messages.info(request, 'Login inválido.')
            return render(request, 'login_form.html', context)

def logout_cliente(request):
    logout(request)
    return redirect('index')

def criar_hash(tamanho=12):
    # Define os caracteres permitidos (letras maiúsculas/minúsculas e números)
    caracteres = string.ascii_letters + string.digits
    
    # Gera a string aleatória de 12 caracteres
    purl = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return purl
        

