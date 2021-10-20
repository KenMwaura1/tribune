from rest_framework import serializers
from .models import ZooMerch


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZooMerch
        fields = ('id', 'name', 'description', 'price')
