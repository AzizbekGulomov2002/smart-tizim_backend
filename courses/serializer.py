from rest_framework import serializers,status
from .models import *
from rest_framework.response import Response
from center.serializer import *
from students.models import Student
from students.serializer import Studentserializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class GroupSerializer(serializers.ModelSerializer):
    student = Studentserializer(many=True,read_only=True)
    course = CourseSerializer(many=True,read_only=True)
    room = RoomSerializer(many=True,read_only=True)
    class Meta:
        model = Groups
        fields = '__all__'
        depth=1
    