from django.shortcuts import render
from django.views.generic import TemplateView


#template view este o clasa dezvoltata de django folosita pentru implementarea si afisarea unui template .html

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'
