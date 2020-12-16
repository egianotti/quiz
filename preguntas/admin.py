from django.contrib import admin
from .models import *
from .views import json

# Register your models here.
def casting(extra,request,queryset):
    p = "H"
    return ('..')

class RespuestaInline(admin.TabularInline):
    list_display = ['respuesta']
    model = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['pregunta']
    inlines = [RespuestaInline]
    actions = [json,casting]




class RespuestaAdmin(admin.ModelAdmin):

#    def get_model_perms(self, request):

      #  Return empty perms dict thus hiding the model from admin index.

        #return {}
      pass



admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Tema)

