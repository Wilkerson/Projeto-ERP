from django.contrib import admin

from erp.models import Funcionario, Produto, Venda

# Register your models here.
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email_funcional', 'remuneracao')
    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco')
    
class VendaAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'produto', 'data_hora')
    
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
    