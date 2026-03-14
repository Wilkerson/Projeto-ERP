from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def home(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        return render(requisicao, template_name='erp/index.html')