
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/', include('app.producto.urls', namespace='index')),
    url(r'^producto/', include('app.producto.urls', namespace='producto')),
    
]
