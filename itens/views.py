from django.shortcuts import render, get_object_or_404

from .models import Itens
from .forms import ContactItens

def index(request):
    itens = Itens.objects.all()
    template_name = 'itens/index.html'
    context = {
        'itens': itens
    }
    return render(request, template_name, context)

# para mostrar na Url o código do item
#def details(request, pk):
#  itens = get_object_or_404(Itens, pk=pk)

def details(request, slug):
    itens = get_object_or_404(Itens, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactItens(request.POST)
        if form.is_valid():
            context['is valid'] = True
            form = ContactItens()
    else:
        form = ContactItens()
        context['form'] = form
        context['itens'] = itens
        template_name = "itens/details.html"
    return render(request, template_name, context)

