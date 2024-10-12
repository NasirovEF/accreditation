from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from sale.models import Product, Factory, Retail, IndEntrepr, Contacts
from sale.serializers import ProductSerializer, FactorySerializer, RetailSerializer, IndEntreprSerializer, \
    ContactsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с продуктами"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с продуктами"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с фабриками"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts.country",]

class RetailViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с розничными точками"""
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts.country", ]


class IndEntreprViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с индивидуальными предпринимателями"""
    queryset = IndEntrepr.objects.all()
    serializer_class = IndEntreprSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts.country",]





