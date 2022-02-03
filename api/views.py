from django.shortcuts import render

from rest_framework import viewsets

from .models import Part, Line, LineData, Spare, Sub_Assembly
from .serializers import PartSerializer, LineSerializer, LineDataSerializer, SpareSerializer, Sub_AssemblySerializer

# Create your views here.

class PartView(viewsets.ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

class LineView(viewsets.ModelViewSet):
    serializer_class = LineSerializer
    queryset = Line.objects.all()

class Sub_AssemblyView(viewsets.ModelViewSet):
    serializer_class = Sub_AssemblySerializer
    queryset = Sub_Assembly.objects.all()

class SpareView(viewsets.ModelViewSet):
    serializer_class = SpareSerializer
    queryset = Spare.objects.all()

class LineDataView(viewsets.ModelViewSet):
    serializer_class = LineDataSerializer
    queryset = LineData.objects.all()

