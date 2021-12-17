from django.urls import path
from cliente import views


urlpatterns = [
    path('nuevo/', views.cliente_view.as_view(), name='cliente_nuevo'),
    path('listar/', views.cliente_list.as_view(), name='cliente_listar'),
    path('editar/<pk>/',views.cliente_edit.as_view(), name='cliente_editar'),
    path('buscar/', views.cliente_buscar, name='cliente_buscar'),
]