from django.shortcuts import HttpResponse, render

from .forms import ContatoForm
from .forms import ProdutoForm

# Create your views here.

#view index
def index(request):
    return render(request,"index.html")

#view sobre
def sobre(request):
   return render(request,"sobre.html")

#view contato
def contato(request):
    if request.method == 'POST':
        print( 'MÉTODO POST')
    else:
        print('MÉTODO GET')
            
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)

#view exibir_item
def exibir_item(request, id):
    
   return render(request,"exibir_item.html",{'id':id})

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
        ],
    }
    return render(request, 'produto/lista.html',contexto)

#view contato
def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/formulario.html', contexto)

def detalhes_produto(request, id):
    contexto = {
        'id': id,
    }
    return render(request, 'produto/detalhes.html', contexto)

def editar_produto(request, id):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/formulario.html', contexto)

def excluir_produto(request, id):
    contexto = {
        'id': id,
    }
    return render(request, 'produto/excluir.html', contexto)










"""
    if request.method == 'POST':
        print( 'MÉTODO POST')
    else:
        print('MÉTODO GET')
"""