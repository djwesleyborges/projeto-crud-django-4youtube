from django.shortcuts import redirect, render

from crm.forms import PessoaForm
from .models import Pessoa

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'lista_pessoas.html', {'pessoas': pessoas})

def nova_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'nova_pessoa.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid:
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})


def excluir_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'excluir_pessoa.html', {'pessoa': pessoa})