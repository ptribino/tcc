from django.shortcuts import render, redirect
from .models import Armario
#from .forms import ArmarioForm
from django.views.generic import ListView
from django_tables2 import RequestConfig
from .tables import ArmarioTable


def armarionew(request, ListView):
    armario = Armario.objects.all()
    template_name = 'armario/armario_form.html'
    context = {
        'armario': armario
    }
    return render(request, template_name, context)

# def details(request, slug):
#     armario = get_object_or_404(Armario, slug=slug)
#     context = {}
#     if request.method == 'POST':
#         form = ArmarioForm(request.POST)
#         if form.is_valid():
#             context['is valid'] = True
#             # print(form.cleaned_data['name'])
#             form = ArmarioForm()
#     else:
#         form = ArmarioForm()
#         context['form'] = form
#         context['armario'] = armario
#         template_name = 'armario/armario_form.html'
#     return render(request, template_name, context)

def get_context_data(self,**kwargs):
    context = super(armarionew, self).get_context_data(**kwargs)
    context['nav_armario']= True
    table = ArmarioTable(Armario.objects.filter(self.kwargs['name']).order_by('name'))
    RequestConfig(self.request, paginate={'per_page':30}).configure(table)
    context['table']=table
    return context