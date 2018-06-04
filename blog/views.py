from django.shortcuts import render
from .models import Blog
from django.http import response
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from . import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


def index(request):
    context = Blog.objects.all()
    return response(request, {'context': context})


class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogModelSerializer
    #permission_classes = IsAdminUser


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogModelSerializer


class BlogViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BlogModelSerializer
    queryset = Blog.objects.all()


class BlogCreate(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  serializers.BlogModelSerializer

