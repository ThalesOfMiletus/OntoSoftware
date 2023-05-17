from django.shortcuts import render

from django.views.generic import TemplateView


class CadastrosViews(TemplateView):
    template_name = 'paginas/cadastro.html'
