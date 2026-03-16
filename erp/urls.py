from django.urls import path
from erp.views import HomeView, ProdutoCreateView, atualiza_funcionario, busca_funcionario_por_id, criar_funcionario, lista_funcionarios

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('funcionarios', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', criar_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),
]
