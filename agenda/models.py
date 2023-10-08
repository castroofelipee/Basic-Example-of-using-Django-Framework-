from django.db import models

# Create your models here.
class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome 
        self.categoria = categoria
        self.local = local 
        self.link = link 

aula_python = Evento("Aula de python", "backend", "Rio de Janeiro")
aula_js = Evento("Aula de JavaScript", "Fullstack", "https://estamosaqui.com")

eventos = [
    aula_python,
    aula_js
]