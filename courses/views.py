from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerandDirectorOrReadOnly
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]
class RoomViewset(ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]
class GroupsViewset(ModelViewSet):
    queryset =  Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
    def create(self, request, *args, **kwargs):
        data = request.data
        group = Groups.objects.create(name=data['name'],education=data.get('education',None),status=data.get('status',None),start=data.get('start',None),finish=data.get('finish',None),user=request.user)
        group.save()
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group.student.add(xona)
                except Student.DoesNotExist:
                    pass

        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        group_object.student.clear()
        group_object.course.clear()
        group_object.room.clear()
        group_object.save()
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education=data.get('education',None)
        group_object.status=data.get('status',None)
        group_object.start=data.get('start',None)
        group_object.finish=data.get('finish',None)
        group_object.user=request.user
        serializer = GroupSerializer(group_object)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education=data.get('education',group_object.education)
        group_object.status=data.get('status',group_object.status)
        group_object.start=data.get('start',group_object.start)
        group_object.finish=data.get('finish',group_object.finish)
        group_object.user=data.get(request.user,group_object.user)
        serializer = GroupSerializer(group_object)
        return Response(serializer.data) 
    def destroy(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.remove(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.remove(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.remove(xona)
                except Student.DoesNotExist:
                    pass
        
        serializer = GroupSerializer(group_object)
        return Response(serializer.data)     
class ClassRoomViewset(ModelViewSet):
    queryset =  ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
    def create(self, request, *args, **kwargs):
        data = request.data
        group = ClassRoom.objects.create(name=data['name'],education=data.get('education',None),status=data.get('status',None),start=data.get('start',None),finish=data.get('finish',None),user=request.user)
        group.save()
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group.student.add(xona)
                except Student.DoesNotExist:
                    pass

        serializer = ClassRoomSerializer(group)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        group_object.student.clear()
        group_object.course.clear()
        group_object.room.clear()
        group_object.save()
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education=data.get('education',None)
        group_object.status=data.get('status',None)
        group_object.start=data.get('start',None)
        group_object.finish=data.get('finish',None)
        group_object.user=request.user
        serializer = ClassRoomSerializer(group_object)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education=data.get('education',group_object.education)
        group_object.status=data.get('status',group_object.status)
        group_object.start=data.get('start',group_object.start)
        group_object.finish=data.get('finish',group_object.finish)
        group_object.user=data.get(request.user,group_object.user)
        serializer = ClassRoomSerializer(group_object)
        return Response(serializer.data) 
    def destroy(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'room' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.remove(xona)
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.remove(xona)
                except Course.DoesNotExist:
                    pass
        if 'student' in data:
            for student in data['student']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.remove(xona)
                except Student.DoesNotExist:
                    pass
        
        serializer = ClassRoomSerializer(group_object)
        return Response(serializer.data)     
                
        
                
        
