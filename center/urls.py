from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import  *
from students.views import *
from courses.views import *
router = DefaultRouter()
router.register('director',DirectorViewset)
router.register('manager',ManagerViewset)
router.register('teacher',TeacherViewset)
router.register('students',StudentViewset)
router.register('course',CourseViewset)
router.register('rooms',RoomViewset)
router.register('groups',GroupsViewset)
router.register('test',TestViewset)
router.register('davomat',DavomatViewset)
urlpatterns = [
    path('',include(router.urls))
]
