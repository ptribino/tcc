from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Armario
from .forms import InsereArmarioForm



class ArmarioListView(ListView):
    template_name = "armario/lista.html"
    model = Armario
    fields = '__all__'
    context_object_name = "armario"


@login_required
def lista(request):
    template_name = 'armario/lista.html'
    return render(request, template_name)


class ArmarioCreateView(CreateView):
    template_name = "armario/cadastra.html"
    model = Armario
    form_class = InsereArmarioForm
    success_url = reverse_lazy("armario:lista_armarios")

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)

    def new_armario(request):
        if request.method == "POST":
            form = InsereArmarioForm(request.POST)
            if form.is_valid():
                newarmario = form.save(commit=False)
                newarmario.user = request.user
                newarmario.descricao = request.descricao
                newarmario.created_at = timezone.now()
                newarmario.save()
                return redirect('armario:lista_armarios', pk=newarmario.pk)
        else:
            form = InsereArmarioForm()
        return render(request, 'armario/atualiza.html', {'form': form})

class ArmarioUpdateView(UpdateView):
    template_name = "armario/atualiza.html"
    model = Armario
    fields = ['name', 'descricao']
    context_object_name = 'armario'
    success_url = reverse_lazy("armario:lista_armarios")


class ArmarioDeleteView(DeleteView):
    template_name = "armario/excluir.html"
    model = Armario
    context_object_name = 'armario'
    success_url = reverse_lazy("armario:lista_armarios")
