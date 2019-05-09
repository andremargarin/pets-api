from rest_framework import viewsets
from .models import Person, Pet
from .serializers import (
    PersonSerializer,
    PetDefaultSerializer,
    PetListSerializer
)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PetListSerializer
        return PetDefaultSerializer
