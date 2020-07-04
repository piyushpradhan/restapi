from rest_framework import serializers
from .models import TitleModel, DescModel

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleModel
        fields = '__all__'

class DescSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescModel
        fields = '__all__'