from django.shortcuts import render, redirect, get_object_or_404
from tecnico.forms import TecnicoForm
from tecnico.forms import EntregaForm
from tecnico.models import Tecnico
from servicio.utileria import render_pdf
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator
# -----importacion para vistas basadas en clases
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy


# Create your views here.

class tecnico_view(CreateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = 'tecnico/tecnico_form.html'
    success_url = reverse_lazy('tecnico_listar')


class tecnico_list(ListView):
    model = Tecnico
    template_name = 'tecnico/tecnico_list.html'
    paginate_by = 7


class tecnico_edit(UpdateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = 'tecnico/tecnico_form.html'
    success_url = reverse_lazy('tecnico_listar')


class informe_edit(UpdateView):
    model = Tecnico
    form_class = EntregaForm
    template_name = 'tecnico/infor_form.html'
    success_url = reverse_lazy('tecnico_listar')


def tecnico_buscar(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        tecnico = Tecnico.objects.filter(cliente__dni__contains=buscar)
        paginator = Paginator(tecnico, 7)
        page = request.GET.get('page')
        tecnico = paginator.get_page(page)
    else:
        tecnico = Tecnico.objects.all()
        paginator = Paginator(tecnico, 7)
        page = request.GET.get('page')
        tecnico = paginator.get_page(page)
    contexto = {'tecnicos': tecnico}
    return render(request, 'tecnico/buscar.html', contexto)


class recibo(View):
    # regresa PDF basada en templae html
    def get(self, request, id_tecnico):
        tecnico = Tecnico.objects.get(id=id_tecnico)
        pdf = render_pdf("tecnico/recibo_pdf.html", {'tecnicos': tecnico})
        return HttpResponse(pdf, content_type='application/pdf')


class pago(View):
    # regresa PDF basada en templae html
    def get(self, request, id_tecnico):
        tecnico = Tecnico.objects.get(id=id_tecnico)
        pdf = render_pdf("tecnico/pago_pdf.html", {'tecnicos': tecnico})
        return HttpResponse(pdf, content_type='application/pdf')
