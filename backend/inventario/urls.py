from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BodegaViewset, CajaViewset, LocalViewset, MarcaViewset, VentaViewset
from .views import ProductoViewset


router = DefaultRouter()
router.register(r'marca', MarcaViewset, )
router.register(r'bodega', BodegaViewset)
router.register(r'caja', CajaViewset, )
router.register(r'productos', ProductoViewset)
router.register(r'local', LocalViewset)
router.register(r'venta', VentaViewset)

urlpatterns = [
    path('', include(router.urls)),

]