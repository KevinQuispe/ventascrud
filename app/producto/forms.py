from django import forms
from app.producto.models import Producto
class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields = [
			'codigo',
			'nombre',
			'descripcion',
			'precio',
			'stock',
		]
		labels = {
			'codigo': 'Codigo',
			'nombre': 'nombre',
			'descripcion': 'descripcion',
			'precio':'precio',
			'stock': 'stock',
			
		}
		#los widgws son los que se van a pintar a forma de etiquetas html
		widgets={
			'codigo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese codigo'}),
			'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese descripcion'}),
			'precio': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese stcok'}),
			'stock': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese stcok'}),
		}	
		