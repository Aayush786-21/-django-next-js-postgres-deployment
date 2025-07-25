from rest_framework import serializers
from .models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = ['id', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
