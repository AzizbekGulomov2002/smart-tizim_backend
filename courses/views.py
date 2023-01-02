from django.shortcuts import render

# Create your views here.
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerandDirectorOrReadOnly
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
class RoomViewset(ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
class GroupsViewset(ModelViewSet):
    queryset =  Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]