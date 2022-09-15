from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from product.models import Product, Order
from product.serializers import (
    ProductSerializer,
    OrderSerializer,
    StatsSerializer
)
from django.utils.dateparse import parse_date
import datetime


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def get_months(start_date, end_date, queryset):
    months = set()
    for order in queryset:
        month = order.get_order_month()
        months.update({month})
    return months


class StatsListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StatsSerializer

    def post(self, request, *args, **kwargs):
        start_date = parse_date(request.data['start_date'])
        end_date = parse_date(request.data['end_date'])
        queryset = Order.objects.filter(
            date__range=[start_date, (end_date + datetime.timedelta(days=1))])

        months = get_months(start_date, end_date, queryset)
        value = 0
        # metric_price = f'/api/stats?date_start={start_date}&date_end={end_date}&metric=price'
        # metric_count = f'/api/stats?date_start={start_date}&date_end={end_date}&metric=count'

        if request.data['metric'] == "count":
            count = []
            for month in months:
                total = {'month': month, 'value': value}
                for order in queryset:
                    if order.get_order_month() == month:
                        for product in order.products.all():
                            total['value'] += 1
                count.append(total)

            context = {
                'start_date': start_date,
                'end_date': end_date,
                "metric=='count'": count
            }
            # redirect(metric_count)
            return Response(context)

        elif request.data['metric'] == "price":
            price = []
            for month in months:
                total = {'month': month, 'value': value}
                for order in queryset:
                    if order.get_order_month() == month:
                        for product in order.products.all():
                            total['value'] += product.price
                total['value'] = float("%.2f" % total['value'])
                price.append(total)

            context = {
                'start_date': start_date,
                'end_date': end_date,
                "metric='price'": price
            }
            # redirect(metric_price)
            return Response(context, status=status.HTTP_200_OK)
