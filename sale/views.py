from django.shortcuts import render
from rest_framework import viewsets

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


class RetailViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с розничными точками"""
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer


class IndEntreprViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с индивидуальными предпринимателями"""
    queryset = IndEntrepr.objects.all()
    serializer_class = IndEntreprSerializer




