from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import StudentPaymentSerializer
from rest_framework.response import Response
class StudentPaymentViewset(ModelViewSet):
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        new_payment= StudentPayment.objects.create(student=Student.objects.get(id=data['student']),user=user,type=data['type'],cost=data['cost'])
        new_payment.save()
        serializer = StudentPaymentSerializer(new_payment)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        payment_data = self.get_object()
        data = request.data
        student = Student.objects.get(id=data['student'])
        payment_data.student=student
        payment_data.cost = data['cost']
        payment_data.user=request.user
        payment_data.type=data['type']
        payment_data.save()
        serializer = StudentPaymentSerializer(payment_data)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        payment_data = self.get_object()
        data = request.data
        student = Student.objects.get(id=data['student'])
        payment_data.student=data.get(student,payment_data.student)
        payment_data.cost = data.get(data['cost'],payment_data.cost)
        payment_data.user=data.get(request.user,payment_data.user)
        payment_data.type=data.get(data['type'],payment_data.type)
        payment_data.save()
        serializer = StudentPaymentSerializer(payment_data)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        payment_date = self.get_object()
        payment_date.delate()
        return Response({'status':'deleted'})
class PaymentViewset(ModelViewSet):
    queryset =  StudentPayment.objects.all()
    serializer_class =  StudentPaymentSerializer
    def list(self, request, *args, **kwargs):
        user = request.user
        objects = StudentPayment.objects.filter(user=user)
        serializer = StudentPaymentSerializer(objects,many=True)
        return Response(serializer.data)