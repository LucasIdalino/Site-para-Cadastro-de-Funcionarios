from django.urls import reverse_lazy
from django.views.generic import *
from helloworld.models import Funcionario
from .forms import InsereFuncionarioForm


class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'


class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


class FuncionariosUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')


class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = "funcionario"
    success_url = reverse_lazy("website:lista_funcionarios")


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")
