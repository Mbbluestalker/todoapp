from django.shortcuts import render
from  .serializers import TodoSerializer
from rest_framework import viewsets
from .models import Todo


class TodoViewset(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    


