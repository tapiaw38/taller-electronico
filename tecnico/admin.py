from django.contrib import admin
from tecnico.models import Tecnico


class TecnicoAdmin(admin.ModelAdmin):
    list_display  =("id","fecha","cliente","producto","marca","modelo","color","serie","entrega")
    search_fields = ["cliente__dni"]
    raw_id_fields = ('cliente',)

# Register your models here.
admin.site.register(Tecnico,TecnicoAdmin)