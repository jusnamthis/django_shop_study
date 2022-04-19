from pipes import Template
from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

class ProductPageView(TemplateView):
    template_name = 'mainapp/products.html'

class ContactsPageView(TemplateView):
    template_name = 'mainapp/contact.html'
