from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from cliente.forms import ClienteForm

from cliente.models import Cliente
from django.http import HttpResponse
from django.core import serializers
#-----importacion para vistas basadas en clases
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy


# Create your views here.

'''
def index(request):
    return render(request, 'cliente/index.html')


def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cliente_listar')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})

def cliente_list(request):
    cliente = Cliente.objects.all()
    contexto = {'clientes':cliente}
    return render(request,'cliente/cliente_list.html',contexto)

def cliente_edit(request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        if request.method == 'GET':
            form = ClienteForm(instance=cliente)
        else:
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
            return redirect('cliente_listar')
        return render(request, 'cliente/cliente_form.html', {'form':form})
'''
class index(TemplateView):
    template_name = 'cliente/index.html'

class cliente_view(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_listar')

class cliente_list(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    paginate_by = 7


class cliente_edit(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_listar')


def cliente_buscar(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        cliente=Cliente.objects.filter(dni__contains=buscar)
        paginator = Paginator(cliente, 7)
        page = request.GET.get('page')
        cliente = paginator.get_page(page)
    else:
        cliente = Cliente.objects.all()
        paginator = Paginator(cliente, 7)
        page = request.GET.get('page')
        cliente = paginator.get_page(page)
    contexto = {'clientes': cliente}
    return render(request, 'cliente/buscar.html',contexto)























