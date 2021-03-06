from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from .helpers import *
import json

# Create your views here.

def json(modeladmin, request, queryset):
    json = []
    for q in queryset:
        json.append({
            'pregunta': q.pregunta,
            'respuestas': list(q.respuestas.all().values_list('respuesta', flat=True))
        })
    return JsonResponse(json, safe=False)

json.short_description = "Exportar selección a JSON"

class PruebaView(View):
    template_name="templates/prueba.html"

    def get(self,request,*args,**kwargs):

        p=request
        context={"p":"hola"}
        return  render(p,self.template_name,context)

    def post (self,request,*args,**kwargs):
        p = request
        context = {"p": "Chau"}
        formatear_json(request)
        return render(p, self.template_name, context)
