__author__ = 'Pavan Kotehal'

from rest_framework.serializers import ModelSerializer
from .models import Blog


class BlogModelSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Blog