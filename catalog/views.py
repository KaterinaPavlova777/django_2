from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactPageView(TemplateView):
    template_name = 'contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
