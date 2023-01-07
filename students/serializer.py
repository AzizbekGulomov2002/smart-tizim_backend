from rest_framework import serializers
from .models import Student,Davomat,Test
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Test
        fields ='__all__'
class Davomatserializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
class Studentserializer(serializers.ModelSerializer):
    davomat =Davomatserializer(many=True,read_only=True)
    class Meta:
        model = Student
        fields ="__all__"

'''
 ["id",
        "name",
        "phone",
        "parent",
        "birth",
        "added",
        "language",
        "address",
        "email",
        "one_id",
        "user",
        "groups",
        "classroom",
        "course",
        'davomat']'''