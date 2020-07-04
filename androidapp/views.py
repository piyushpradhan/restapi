from django.shortcuts import render
from rest_framework import viewsets
from .models import TitleModel, DescModel
from .serializers import TitleSerializer, DescSerializer

class TitleViewSet(viewsets.ModelViewSet):
    queryset = TitleModel.objects.all()
    serializer_class = TitleSerializer

class DescViewSet(viewsets.ModelViewSet):
    queryset = DescModel.objects.all()
    serializer_class = DescSerializer