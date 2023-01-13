from rest_framework import serializers
from .models import Student,Davomat,Test
from center.serializer import ManagerSerializer
from center.models import User
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Test
        fields ='__all__'
class Davomatserializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
        depth=1
class Studentserializer(serializers.ModelSerializer):
    davomat =Davomatserializer(many=True,read_only=True)
    last_payment = serializers.SerializerMethodField()

    def get_last_payment(self, obj):
        return obj.tolov
    class Meta:
        model = Student
        fields ="__all__"
        read_only_fields = ['id', 'user']
        depth=1

    def create(self, validated_data):
        user= self.context["request"].user
        student = Student.objects.create(**validated_data,user=user)
        return student
