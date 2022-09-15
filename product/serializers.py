from rest_framework import serializers
from product.models import Product, Order, Stats, Metric
from enumchoicefield import ChoiceEnum, EnumChoiceField


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderProductSerializer(
    serializers.PrimaryKeyRelatedField, serializers.ModelSerializer
):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ('id', 'date', 'products')


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ('id', 'start_date', 'end_date', 'metric')

    start_date = serializers.DateField()
    end_date = serializers.DateField()
    metric = EnumChoiceField(enum_class=Metric)

