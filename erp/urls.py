from django.urls import path
from erp.views import home

app_name = 'erp'

urlpatterns = [
    path('', home)
]
