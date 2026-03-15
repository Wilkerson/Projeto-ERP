from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from erp.forms import FuncionarioForm
from erp.models import Funcionario

# Create your views here.

def home(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        return render(requisicao, template_name='erp/index.html')
    
def criar_funcionario(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = FuncionarioForm()
        return render(requisicao, template_name='erp/funcionarios/novo.html', context={'form': form})
    elif requisicao.method == 'POST':
        form = FuncionarioForm(requisicao.POST)
        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            funcionario.save()
            return HttpResponseRedirect(redirect_to='/')
        
def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()
        return render(requisicao, template_name='erp/funcionarios/lista.html', context={'funcionarios': funcionarios})
    
def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
            
        return render(requisicao, template_name='erp/funcionarios/detalhe.html', context={'funcionario': funcionario})