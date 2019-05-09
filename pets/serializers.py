from rest_framework import serializers
from .models import Person, Pet


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'resource_uri')


class PetDefaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'resource_uri', 'person')


class PetListSerializer(PetDefaultSerializer):
    person = PersonSerializer()
