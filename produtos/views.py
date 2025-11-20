from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Produto

def inserir_produto(request: HttpRequest):
    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")

        produto = Produto(nome=nome, preco=preco)
        produto.save()

        return redirect('listar_produtos')

    return render(request, 'inserir_produto.html', {
        'nome': 'Usuário'})
 
    
def editar_produto(request: HttpRequest, id: int):
    produto = Produto.objects.get(id=id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")

        produto.nome = nome
        produto.preco = preco
        produto.save()

        return redirect('listar_produtos')

    return render(request, 'inserir_produto.html', {'produto': produto})


def ver_produto(request: HttpRequest, id: int):
    produto = Produto.objects.get(id=id)
    return render(request, 'ver_produto.html', {'produto': produto})


def listar_produtos(request: HttpRequest):
    produtos = Produto.objects.all().order_by('-preco')
    return render(request, 'listar_produtos.html', {'produtos': produtos})


def excluir_produto(request: HttpRequest, id: int):
    produto = Produto.objects.get(id=id)

    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'confirmar_exclusao.html', {'produto': produto})

