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

# LISTA ARMÁRIOS CADASTRADOS
@login_required
def lista(request):
    template_name = 'armario/lista.html'
    return render(request, template_name)

def get_object(self, queryset=None):
    armario = None
    id = self.kwargs.get(self.pk_url_kwarg)
    user_id = self.kwargs.get(self.pk_url_kwarg)
    armario = Armario.objects.filter(user_id=user_id).first()

    return armario

#CRIACAO DO ARMARIO(CABEÇALHO)
class ArmarioCreateView(CreateView):
    template_name = "armario/cadastra.html"
    model = Armario
    form_class = InsereArmarioForm
    success_url = reverse_lazy("armario:lista_armarios")

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)

    def new_armario(request, armario_id):
        newarmario = Armario.objects.get(id=armario_id)
        user = request.user.id
        if request.method == "POST":
            form = InsereArmarioForm(data=request.POST,user=request.user, instance=newarmario)
            if form.is_valid():
                newarmario = form.save(commit=False)
                newarmario.name = request.name
                newarmario.descricao = request.descricao
                newarmario.created_at = timezone.now()
                newarmario.save()
                return redirect('armario:lista_armarios', pk=newarmario.pk)
        else:
            form = InsereArmarioForm(user=request.user, instance=newarmario)
        return render(request, 'armario/atualiza.html', {'form': form})

    # def post(self, request):
    #     data={}
    #     data['name'] = request.POST['name']
    #     data['descricao'] = request.POST['descricao']
    #     data['armario_id'] = request.POST['armario_id']
    #
    #
    #     if data['armario_id']:
    #         armario = Armario.objects.get(id=data['armario_id'])
    #         armario.name = data['name']
    #         armario.descricao = data['descricao']
    #         armario.save()
    #     else:
    #         armario = Armario.objects.create(
    #             name=data['name'], descricao=data['descricao']
    #         )

    #     itens = armario.armarioitem.set.all()
    #     data['armario'] = armario
    #     data['itens'] = itens
    #     return render(
    #         request, 'armario/lista.html', data
    #     )



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
