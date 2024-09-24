from django.db import models
from django.core.exceptions import ValidationError
from authentification.models import User

class Marca(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bodega(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Caja(models.Model):
    referencia = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)  # Relacionado correctamente con Bodega
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.referencia

class Producto(models.Model):
    codigo = models.CharField(max_length=100)
    talla = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    precio_mayor = models.DecimalField(max_digits=10, decimal_places=2)
    precio_detal = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        # Sumar el stock de todos los productos con el mismo código en la misma caja
        total_stock = Producto.objects.filter(caja=self.caja, codigo=self.codigo).aggregate(total=models.Sum('stock'))['total'] or 0
        if total_stock + self.stock > self.caja.cantidad:
            raise ValidationError({'stock': "La cantidad del producto no puede exceder la cantidad disponible en la caja."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.talla}"

class Local(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)  # Relacionado con una bodega

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)  # Donde se realizó la venta
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return f"Venta de {self.cantidad} {self.producto.codigo} en {self.local.nombre}"