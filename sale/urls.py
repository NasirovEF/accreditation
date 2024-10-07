from django.urls import path
from rest_framework.routers import DefaultRouter
from sale.apps import SaleConfig
from sale.views import FactoryViewSet, RetailViewSet, ProductViewSet, IndEntreprViewSet

app_name = SaleConfig.name

router = DefaultRouter()
router.register(r'factory', FactoryViewSet, basename='factory')
router.register(r'retail', RetailViewSet, basename='retail')
router.register(r'indentrepr', IndEntreprViewSet, basename='indentrepr')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [] + router.urls
