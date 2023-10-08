from django.shortcuts import render
from django.http.response import HttpResponse
from agenda.models import eventos
from django.template import loader

# Create your views here.


def exibir_eventos(request):
   evento = eventos[0]
   template = loader.get_template("agenda/exibir_evento.html")
   rendered_template = template.render(context={"evento": evento}, request=request)
   return HttpResponse(rendered_template)


def index(request):
    return HttpResponse("Olá, Mundo!")
    