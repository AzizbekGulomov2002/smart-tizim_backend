from rest_framework import serializers
from .models import StudentPayment
class StudentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPayment
        fields = '__all__'
