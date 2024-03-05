from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bogis_nails.product.models import Product

from bogis_nails.product.forms import ProductForm


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products.html'
    

class DetailsProductView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/details_product.html'
    

class AddProductView(CreateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/add_product.html'

    def get_success_url(self):
       return reverse_lazy('details product', kwargs={
           'pk': self.object.pk
       })
            

class EditProductView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/edit_products.html'
    
    def get_success_url(self):
        return reverse_lazy('details product', kwargs={
            'pk': self.object.pk
        })


class DeleteProductView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def delete(self, request, *args, **kwargs):
        # Delete object and redirect to success URL
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)