from django.urls import path
from tecnico import views
from tecnico.views import recibo
from tecnico.views import pago


urlpatterns = [
    path('nuevo/', views.tecnico_view.as_view(), name='tecnico_nuevo'),
    path('listar/', views.tecnico_list.as_view(), name='tecnico_listar'),
    path('editar/<pk>/',views.tecnico_edit.as_view(), name='tecnico_editar'),
    path('informe/<pk>/', views.informe_edit.as_view(), name='informe_editar'),
    path('buscar/', views.tecnico_buscar, name='tecnico_buscar'),
    path('recibo/<str:id_tecnico>/', recibo.as_view(), name='recibo_pdf'),
    path('pago/<str:id_tecnico>/', pago.as_view(), name='pago_pdf'),
]
