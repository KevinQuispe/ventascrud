from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from app.producto.models import Producto
from app.producto.forms import ProductoForm
# Create your views here.
def index(request):
    return render(request,'producto/index.html')
    
class ProductoCreate(CreateView):
   	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_crear.html'
	success_url = reverse_lazy('producto:producto_listar')
	
class ProductoListar(ListView):
	model = Producto
	template_name='producto/producto_listar'
	paginate_by =2

class ProductoUpdate(UpdateView):
	model=Producto
	form_class=ProductoForm
	template_name='producto/producto_crear.html'
	success_url=reverse_lazy ('producto:producto_listar')

class ProductoDelete(DeleteView):
	model=Producto
	template_name='producto/producto_delete.html'
	success_url = reverse_lazy('producto:producto_listar')


   