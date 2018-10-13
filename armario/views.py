from django.shortcuts import render, redirect
from .models import Armario
#from .forms import ArmarioForm


def armarionew(request):
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
