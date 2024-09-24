from rest_framework import serializers
from django.db.models import Sum  # Importar Sum para la agregación
from .models import Bodega, Caja, Marca, Producto,Local, Venta

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate(self, data):
        caja = data.get('caja')
        cantidad_producto = data.get('stock')
        codigo_producto = data.get('codigo')

        if caja and cantidad_producto is not None:
            # Obtener el objeto Caja actual desde la base de datos
            caja_obj = Caja.objects.get(pk=caja.pk)
            
            # Sumar el stock de todos los productos con el mismo código en la misma caja
            total_stock = Producto.objects.filter(caja=caja, codigo=codigo_producto).aggregate(total=Sum('stock'))['total'] or 0

            if total_stock + cantidad_producto > caja_obj.cantidad:
                raise serializers.ValidationError(
                    {"stock": "La cantidad del producto no puede exceder la cantidad disponible en la caja."}
                )
        
        return data
    
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'