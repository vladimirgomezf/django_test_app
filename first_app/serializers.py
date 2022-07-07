from django.contrib.auth.models import User, Group
from rest_framework import serializers

from first_app.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ["street", "city", "state", "zip", "country"]

    # def create(self, validated_data):
    #     return Address.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.street = validated_data.get('street', instance.street)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.zip = validated_data.get('zip', instance.zip)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.save()
    #     return instance