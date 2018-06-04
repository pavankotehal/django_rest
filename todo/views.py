from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework import viewsets
from .models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer