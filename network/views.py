from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from network.models import Link, Item
from .serializers import LinkSerializer, ItemSerializer

class LinksViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filterset_fields = ['country']

class ItemsViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
