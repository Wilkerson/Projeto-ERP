from django.urls import path
from erp.views import criar_funcionario, home

app_name = 'erp'

urlpatterns = [
    path('', home),
    path('funcionarios/novo', criar_funcionario)
]
