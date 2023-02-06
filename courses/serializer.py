from rest_framework import serializers,status
from .models import *
from rest_framework.response import Response
from center.serializer import *
from students.models import Student
from students.serializer import Studentserializer
class CourseSerializer(serializers.ModelSerializer):
    students_count= serializers.SerializerMethodField()
    groups_count = serializers.SerializerMethodField()
    def get_students_count(self, obj):
        return obj.student_count
    def get_groups_count(self, obj):
        return obj.group_count
    class Meta:
        model = Course
        fields = ['id','name','cost','students_count','groups_count']
        read_only_fields = ['id','students_count','groups_count']
class RoomSerializer(serializers.ModelSerializer):
    groups_count = serializers.SerializerMethodField()
    def get_groups_count(self, obj):
        return obj.group_count
    class Meta:
        model = Room
        fields = ['id','name','student_count','groups_count']
        read_only_fields = ['id','groups_count']
class GroupSerializer(serializers.ModelSerializer):
    student = Studentserializer(many=True,read_only=True)
    # course = CourseSerializer(many=True,read_only=True)
    # room = RoomSerializer(many=True,read_only=True)
    class Meta:
        model = Groups
        fields = '__all__'
        depth=1
class ClassRoomSerializer(serializers.ModelSerializer):
    student = Studentserializer(many=True,read_only=True)
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth=1
    