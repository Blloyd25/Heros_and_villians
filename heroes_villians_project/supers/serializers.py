
from rest_framework import serializers
from .models import Supers

class Supers_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']