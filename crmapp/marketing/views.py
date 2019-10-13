from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePage(TemplateView):
    '''This will return the template name since the pages is not that cmplex'''

    template_name = 'marketing/home.html'
