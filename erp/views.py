from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from erp.forms import FuncionarioForm, ProdutoForm
from erp.models import Funcionario, Produto

# Create your views here.  
class HomeView(TemplateView):
    template_name = 'erp/index.html'
    
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
    
def atualiza_funcionario(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
            
        form = FuncionarioForm(instance=funcionario)
        return render(requisicao, template_name='erp/funcionarios/atualiza.html', context={'form': form})
    elif requisicao.method == 'POST':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
            
        form = FuncionarioForm(requisicao.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')
        
class ProdutoCreateView(CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')