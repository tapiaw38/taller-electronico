from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display  =("id","nombre","dni","direccion","correo","telefono")
    search_fields = ["nombre","dni"]


# Register your models here.
admin.site.register(Cliente,ClienteAdmin)