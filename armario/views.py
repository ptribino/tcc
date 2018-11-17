from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Armario
from .forms import InsereArmarioForm


class ArmarioListView(ListView):
    template_name = "armario/lista.html"
    model = Armario
    fields = '__all__'
    context_object_name = "armario"


class ArmarioCreateView(CreateView):
    template_name = "armario/cadastra.html"
    model = Armario
    form_class = InsereArmarioForm
    success_url = reverse_lazy("armario:lista_armarios")


class ArmarioUpdateView(UpdateView):
    template_name = "armario/atualiza.html"
    model = Armario
    fields = '__all__'
    context_object_name = 'armario'
    success_url = reverse_lazy("armario:lista_armarios")


class ArmarioDeleteView(DeleteView):
    template_name = "armario/excluir.html"
    model = Armario
    context_object_name = 'armario'
    success_url = reverse_lazy("armario:lista_armarios")
