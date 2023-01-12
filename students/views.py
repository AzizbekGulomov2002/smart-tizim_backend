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
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsManagerandDirectorOrReadOnly]

    def get_serializer_context(self):
        # this is the trick since you want to pass the request object to your serializer
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class DavomatViewset(ModelViewSet):
    queryset =  Davomat.objects.all()
    serializer_class = Davomatserializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]