from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

app_name = 'product'

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls
