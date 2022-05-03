from pipes import Template
from django.views.generic.base import TemplateView
from .models import Category, Product

# Create your views here.

MENU_LINKS = {
    "main": "Главная",
    "products": "Продукты",
    "contact": "Контакты",
}

PRODUCTS = [
    {
        'name': 'Chair 1',
        'img': 'img/product-11.jpg',
        'description': 'Very durable chair',
    },
    {
        'name': 'Chair 2',
        'img': 'img/product-21.jpg',
        'description': 'Pretty durable chair',
    },
    {
        'name': 'Chair 3',
        'img': 'img/product-31.jpg',
        'description': 'Such a durable chair',
    },
    {
        'name': 'Chair 4',
        'img': 'img/product-31.jpg',
        'description': 'Badly chair',
    },
]


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU_LINKS
        context["title"] = "Главная"
        context["greeting"] = "yo creator!"
        return context


class ProductPageView(TemplateView):
    template_name = "mainapp/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU_LINKS
        context["title"] = "Продукты"
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU_LINKS
        context["title"] = "Контакты"
        return context
