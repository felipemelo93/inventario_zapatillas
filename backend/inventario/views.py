from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Bodega, Caja, Local, Marca, Venta
from .models import Producto
from .serializers import BodegaSerializer, CajaSerializer, LocalSerializer, MarcaSerializer, VentaSerializer
from .serializers import ProductoSerializer
from rest_framework.exceptions import ValidationError

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticated]

class BodegaViewset(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    permission_classes = [IsAuthenticated]    


class CajaViewset(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        return Caja.objects.filter(usuario=self.request.user)
    
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Se realiza validación en el serializer
        serializer.save()

    def perform_update(self, serializer):
        # Se realiza validación en el serializer
        serializer.save()
        
class LocalViewset(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated]

class VentaViewset(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]
    #def get_queryset(self):
        #return Producto.objects.filter(usuario=self.request.user)

    