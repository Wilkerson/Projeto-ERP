from django.urls import path
from erp.views import busca_funcionario_por_id, criar_funcionario, home, lista_funcionarios

app_name = 'erp'

urlpatterns = [
    path('', home),
    path('funcionarios', lista_funcionarios),
    path('funcionarios/novo', criar_funcionario),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id)
]
