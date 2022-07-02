from django.contrib.auth.models import User, Group
from rest_framework import serializers

from first_app.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ["street", "city", "state", "zip", "country"]
