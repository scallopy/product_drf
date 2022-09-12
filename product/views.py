from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import generics
from product.models import Product, Order
from product.serializers import ProductSerializer, OrderSerializer
# import datetime
# from enum import Enum


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderMonth(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_month(self, request, *args, **kwargs):
        print(request.pk)
        queryset = Order.objects.filter(pk=request.pk)
        return self.retrieve(request, *args, **kwargs)


"""
class StatsViewSet(viewsets.ModelViewSet):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def filter_data(request, queryset, pk):
        start_date = request.get_object().start_date
        end_date = request.get_object().end_date
        queryset = Order.objects.filter(
            date__range=[start_date, (end_date + datetime.timedelta(days=1))])
        value = 0
        price_count = {}
        order_prices_count = []
        order_months = [month for month in range(start_date.month, (end_date.month + 1))]
        for month in order_months:
            for order in queryset:
                if order.date.month == month:
                    order_month = f"{order.date.year}  {order.date.month}"
                    price = {'month': order_month, 'value': value}
                    for product in order.products.all():
                        if order.date.month == month:
                            value += float(product.price)
                            price['value'] = value
                    print(price)
        order_prices_count.append(price)
        print(order_prices_count)
        price_count.update({'order': order_prices_count})

        return Response(price_count.values())

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def filter_months(request, queryset, pk):
        start_date = request.get_object().start_date
        end_date = request.get_object().end_date
        queryset = Order.objects.filter(
            date__range=[start_date, (end_date + datetime.timedelta(days=1))])
        count = 0
        return Response(queryset)
"""
