from rest_framework import serializers

from sale.models import Product, Contacts, Factory, Retail, IndEntrepr


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с продуктом"""
    class Meta:
        model = Product
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с контактами"""
    class Meta:
        model = Contacts
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с фабрикой"""
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(many=False)

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        factory = Factory.objects.create(contacts=contacts, **validation_data)
        return factory

    class Meta:
        model = Factory
        fields = "__all__"


class RetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с розничной точки"""
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(many=False)
    arrears = serializers.FloatField(read_only=True)

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        retail = Retail.objects.create(contacts=contacts, **validation_data)
        return retail

    class Meta:
        model = Retail
        fields = "__all__"


class IndEntreprSerializer(serializers.ModelSerializer):
    """Сериалайзер индивидуального предпринимателя"""
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(many=False)
    arrears = serializers.FloatField(read_only=True)

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        indentrepr = IndEntrepr.objects.create(contacts=contacts, **validation_data)
        return indentrepr

    class Meta:
        model = IndEntrepr
        fields = "__all__"
