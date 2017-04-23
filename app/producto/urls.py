from django.conf.urls import url,include
from app.producto.views import index,ProductoCreate,ProductoListar,ProductoUpdate,ProductoDelete
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^nuevo/',ProductoCreate.as_view(),name='producto_crear'),
    url(r'^listar/',ProductoListar.as_view(),name='producto_listar'),
    url(r'^editar/(?P<pk>\d+)/$',ProductoUpdate.as_view(),name='producto_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ProductoDelete.as_view(),name='producto_delete'),
   ]