from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),

    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),

    path('funcionario/<pk>', FuncionariosUpdateView.as_view(), name='atualiza_funcionario'),

    #path('funcionario/<slug>', FuncionariosUpdateView.as_view(), name='atualiza_funcionario'),

    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),

    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario')
]
