from django.shortcuts import render
from courses.permissions import IsManagerandDirectorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import * 
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import codecs
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
fs = FileSystemStorage(location='tmp/')
from rest_framework.decorators import action
class TestViewset(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES["file"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        results_list = []
        for id_, row in enumerate(reader):
            (
                test_kodi,
                fan_nomi,
                talaba,
                telefon_raqam,
                savollar_soni,
                togri_javoblar
            ) = row
            results_list.append(
                Test(
                    test_kodi=test_kodi,
                    fan_nomi=fan_nomi,
                    talaba=talaba,
                    telefon_raqam=telefon_raqam,
                    savollar_soni=savollar_soni,
                    togri_javoblar=togri_javoblar,
                )
            )
        print(results_list)
        Test.objects.bulk_create(results_list)
        return Response("Successfully upload the data")
    @action(detail=False, methods=['POST'])
    def upload_data_with_validation(self, request):
        file = request.FILES.get("file")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        results_list = []
        for row in serializer.data:
            results_list.append(
                Test(
                    test_kodi=row["test_kodi"],
                    fan_nomi=row["fan_nomi"],
                    talaba=row["talaba"],
                    telefon_raqam = row['telefon_raqam'],
                    savollar_soni=row["savollar_soni"],
                    togri_javoblar=row["togri_javoblar"],

                )
            )

        Test.objects.bulk_create(results_list)

        return Response("Successfully upload the data")
class StudentViewset(ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = Studentserializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
class DavomatViewset(ModelViewSet):
    queryset =  Davomat.objects.all()
    serializer_class = Davomatserializer
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            student = Student.objects.get(id=data['student'])
            davomat = Davomat.objects.create(student=student,description=data.get('description',None),status=data.get('status',None),date=data.get('date',datetime.now()))
            serializer = Davomatserializer(davomat)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response('Student not found')
    def partial_update(self, request, *args, **kwargs):
        davomat_data = self.get_object()
        data = request.data
        if 'student' in data:
            try:
                student = Student.objects.get(id=data['student'])
                davomat_data.student =student
                davomat_data.description = data.get('description',davomat_data.description)
                davomat_data.status = data.get('status',davomat_data.status)
                davomat_data.date = data.get('date',davomat_data.date)
                serializer = Davomatserializer(davomat_data)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response('Student not found')
        else:
            return Response('student field required')
    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
            
        
        
