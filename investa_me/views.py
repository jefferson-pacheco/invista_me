from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import Investimento
from .forms import InvestimentoForm



def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('tipoInvestimento')
    }
    
    return render(request, 'investimentos/investimento_registrado.html', investimento)

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    investimento = get_object_or_404(Investimento, pk=id_investimento)
    dados = {
        'investimento': investimento
    }
    return render(request, 'investimentos/detalhe.html', context=dados)

def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)
    
def editar(request,id_investimento):
    investimento = get_object_or_404(Investimento, pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request, id_investimento):
    investimento = get_object_or_404(Investimento, pk=id_investimento) 
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos') 
    return render(request, 'investimentos/confirmar_exclusao.html', {'item':investimento})                    
    