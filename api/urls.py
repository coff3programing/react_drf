from django.urls import path, include
from rest_framework import routers
from .views import LaboratorioViewSet, MarcaViewSet, ActivoViewSet

router = routers.DefaultRouter()
router.register(r'laboratorios', LaboratorioViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'activos', ActivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]