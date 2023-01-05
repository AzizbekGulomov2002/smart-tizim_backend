from django.shortcuts import render

from courses.permissions import IsManagerandDirectorOrReadOnly
# Create your views here.
from .models import * 
from .serializer import *
from rest_framework.viewsets import ModelViewSet
class StudentViewset(ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class =  Studentserializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
class DavomatViewset(ModelViewSet):
    queryset =  Davomat.objects.all()
    serializer_class = Davomatserializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]