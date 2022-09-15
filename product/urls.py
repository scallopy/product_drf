from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'product'

router = DefaultRouter()

router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', views.StatsListApiView.as_view())
]
