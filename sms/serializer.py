from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
# from yaml import serializers

from .models import *

#  fields = ['department_name'] #which fields you have to serialize


class ParentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parent
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classroom
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Grade
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Attendance
        fields = '__all__'

class ClassroomStudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassroomStudent
        fields = '__all__'

class ExamTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExamType
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choice
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exam
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'

class ExamResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExamResult
        fields = '__all__'

class AdminSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AdminSection
        fields = '__all__'