from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from erp.forms import FuncionarioForm, ProdutoForm
from erp.models import Funcionario, Produto, Venda

class ErpLoginView(LoginView):
    template_name = 'erp/login.html'
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True
    
class ErpLogoutView(LogoutView):
    template_name = 'erp/logout.html'
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'erp/dashboard.html'

# Create your views here.  
class HomeView(TemplateView):
    template_name = 'erp/index.html'
 
@login_required   
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

@login_required         
def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()
        return render(requisicao, template_name='erp/funcionarios/lista.html', context={'funcionarios': funcionarios})

@login_required     
def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
            
        return render(requisicao, template_name='erp/funcionarios/detalhe.html', context={'funcionario': funcionario})

@login_required     
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
        
class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'erp/produtos/novo.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')
    
class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'erp/produtos/lista.html'
    context_object_name = 'produtos'
    
class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'erp/produtos/atualiza.html'
    success_url = reverse_lazy('erp:lista_produtos')
    
class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'
    
    def get_object(self, queryset = None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')
    
    def get_object(self, queryset = None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:home')
    fields = ['produto', 'funcionario']
    
class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'
    
class VendaDetailView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'
    
    def get_object(self, queryset = None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')
    
    def get_object(self, queryset = None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
class VendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = '__all__'
    success_url = reverse_lazy('erp:lista_vendas')