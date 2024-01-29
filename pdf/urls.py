from django.urls import path, include
from . import views
#djangorestframework
from rest_framework import routers
from .api import FacturaViewSet

#djangorestframework
router = routers.DefaultRouter()
router.register('api/facturas', FacturaViewSet, 'facturas-api')

urlpatterns = [
    path('facturas/', views.facturas, name='facturas'),
    path('facturas/reporte/<int:id>', views.generar_pdf, name='generate_pdf'),
    path("table/", views.table, name='table'),

    path("", include(router.urls)),
]