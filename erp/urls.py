from django.urls import path
from erp.views import HomeView, atualiza_funcionario, busca_funcionario_por_id, criar_funcionario, lista_funcionarios

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view()),
    path('funcionarios', lista_funcionarios),
    path('funcionarios/novo', criar_funcionario),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario),
]
