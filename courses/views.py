from django.shortcuts import render

# Create your views here.
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class RoomViewset(ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class = RoomSerializer
class GroupsViewset(ModelViewSet):
    queryset =  Groups.objects.all()
    serializer_class = GroupSerializer