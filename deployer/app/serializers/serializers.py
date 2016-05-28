from moneyed import Money
from django.contrib.auth.models import User, Group
from app.models import Server, Application
from rest_framework import serializers
import string


class MoneyField(serializers.Field):
    def to_representation(self, obj):
        return "{} {}".format(obj.amount, obj.currency)

    def to_internal_value(self, data):
        price = string.split(data, " ")
        return Money(price[0], price[1])


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    costs = MoneyField()

    class Meta:
        model = Server
        fields = ('name', 'ip', 'path', 'costs')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    price = MoneyField()

    class Meta:
        model = Application
        fields = ('name', 'database', 'price', 'servers')
