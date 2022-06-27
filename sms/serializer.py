from dataclasses import field
from pyexpat import model
from rest_framework import serializers
# from yaml import serializers

from .models import *

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department #which model you have to serialize
        fields = '__all__' #which fields you have to serialize

class DepartmentChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department #which model you have to serialize
        fields = ['department_name'] #which fields you have to serialize

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'