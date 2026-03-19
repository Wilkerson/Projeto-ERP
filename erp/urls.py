from django.urls import path
from core import settings
from erp.views import HomeView, ProdutoCreateView, ProdutoDeleteView, ProdutoDetailView, ProdutoListView, ProdutoUpdateView, VendaCreateView, VendaDeleteView, VendaDetailView, VendaListView, VendaUpdateView, atualiza_funcionario, busca_funcionario_por_id, criar_funcionario, lista_funcionarios
from django.conf.urls.static import static

app_name = 'erp'

urlpatterns = [
    #FUNCIONÁRIOS
    path('', HomeView.as_view(), name='home'),
    path('funcionarios', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', criar_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),
    #PRODUTOS
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),
    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/atualiza/<pk>', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deleta/<pk>', ProdutoDeleteView.as_view(), name='deleta_produto'),
    #VENDAS
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),
    path('vendas/', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhe_venda'),
    path('vendas/deleta/<pk>', VendaDeleteView.as_view(), name='deleta_venda'),
    path('vendas/atualiza/<pk>', VendaUpdateView.as_view(), name='atualiza_venda'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
