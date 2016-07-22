from moneyed import Money
from django.contrib.auth.models import User, Group
from app.models import Server, Application, Address, Invoice, InvoiceItem
from rest_framework import serializers


class MoneyField(serializers.Field):
    def to_representation(self, obj):
        return "{} {}".format(obj.amount, obj.currency)

    def to_internal_value(self, data):
        price = data.split(" ")
        return Money(price[0], price[1])


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Group
        fields = ('url', 'name', 'url')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'url')


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    costs = MoneyField()

    class Meta:
        model = Server
        fields = ('name', 'ip', 'path', 'costs', 'url')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    price = MoneyField()

    class Meta:
        model = Application
        fields = ('name', 'path', 'database', 'price', 'billTo', 'billDate', 'servers', 'url')


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    #invoiceItems = serializers.StringRelatedField(many=True)

    class Meta:
        model = Invoice
        fields = ('date', 'dueDate', 'invoiceNo', 'billTo', 'invoiceItems', 'url')


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    price = MoneyField()

    class Meta:
        model = InvoiceItem
        fields = ('title', 'price', 'vat', 'invoice', 'url')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Address
        fields = ('name', 'street', 'city', 'postal_code', 'tax_id', 'url')
