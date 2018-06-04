__author__ = 'Pavan Kotehal'

from rest_framework import serializers
from .models import ToDo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ToDo