from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=100)

    class Meta:
        model = Todo
        fields = ['id', 'task', 'created_at', 'user']
        read_only_fields = ('id', 'created_at', 'user',)
