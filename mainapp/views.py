from pipes import Template
from django.views.generic.base import TemplateView

# Create your views here.

MENU_LINKS = {
    "main": "Главная",
    "products": "Продукты",
    "contact": "Контакты",
}


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
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU_LINKS
        context["title"] = "Контакты"
        return context
