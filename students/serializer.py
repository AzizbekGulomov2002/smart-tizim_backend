from rest_framework import serializers
from .models import Student,Davomat
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