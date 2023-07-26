from rest_framework import serializers
from .models import Student, Course, Teacher
from django.contrib.auth.models import User


class CourseSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=100)   
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    start_date = serializers.DateField()
    end_date = serializers.DateField()  



 # object level validation
    # def validate(self, attrs):
    #     if attrs['duration'] != "3 months" :
    #         raise serializers.ValidationError("please duration must be 3 months")
    #     return super().validate(attrs)

    def validated_price(self, value):
        if not isinstance(value, [float]):
            raise serializers.ValidationError("Only decimals are allowed")
    
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.duration=validated_data.get(' duration', instance. duration)
        instance.price=validated_data.get('price', instance.price)
        instance.start_date=validated_data.get('start_date', instance.start_date)
        instance.end_date=validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
    

class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Student
        fields=["first_name","last_name","gender","Age","email"]



class TeacherSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Teacher
        fields=["name","gender","course"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]       