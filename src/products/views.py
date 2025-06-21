from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render
 
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context["title"] = " Practica 54 - List View"
        return context

class ProductDetailView(DetailView):
    model = Product

class ProtectedListView(LoginRequiredMixin, ListView):
    model = Product
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context["title"] = " Practica 54 - List View Protejido"
        return context
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)