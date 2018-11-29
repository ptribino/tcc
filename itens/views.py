from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Itens
from .forms import ContactItens

# class ItensListView(generic.ListView):
#
#     model = Itens
#     template_name = 'itens/index.html'
#
# itens_list = ItensListView.as_view()

def index(request):
    itens = Itens.objects.all()
    template_name = 'itens/lista_itens.html'
    context = {
        'itens': itens
    }
    return render(request, template_name, context)


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
