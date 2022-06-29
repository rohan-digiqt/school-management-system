
from ast import Sub
from copyreg import constructor
from pyexpat import model
from unicodedata import name
from dbus import MissingErrorHandlerException
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from sms import constant

# Create your models here.

class Parent(models.Model):
    email = models.EmailField()
    # password = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.IntegerField()
    is_active = models.BooleanField(default=False)



class Teacher(models.Model):
    email = models.EmailField()
    # password = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.IntegerField()
    is_active = models.BooleanField(default=False)


class Classroom(models.Model):
    # year = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    remarks = models.TextField(max_length=100)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key



class Grade(models.Model):
    grade = models.CharField(max_length=10)



class ExamType(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()


class Choice(models.Model):
    if name == 'Degree Engineering' or name == 'Diploma Engineering':
        sub_cource = models.CharField(max_length=20, choices=constant.CHOICE_1)      
    elif name == 'B.Sc.':
        sub_cource = models.CharField(max_length=20, choices=constant.CHOICE_1)
    else:
        sub_cource = models.CharField(max_length=20, choices='')
        


    

    
class Course(Choice,models.Model):
    COURSE_CHOICE = (
        ('Degree Engineering','Degree Engineering'),
        ('Diploma Engineering','Diploma Engineering'),
        ('B.Sc.','B.Sc.'),
        ('B.Pharm','B.Pharm'),
        ('MCA','MCA')
    )

    name = models.CharField(max_length=20, choices=COURSE_CHOICE)
    description = models.TextField()
    fees = models.IntegerField()






class Exam(models.Model):
    type = models.ForeignKey(ExamType, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)

class Subject(models.Model):
    
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)


class Student(models.Model):
    
    enrollment = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    dob = models.DateField()
    mobile_no = models.IntegerField()
    parent = models.ForeignKey(Parent, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    joining_date = models.DateField() #joining date
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False) #is_active
    # subject, cource

class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    is_active = models.BooleanField(default=False)
    remarks = models.TextField()

class ClassroomStudent(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE) #Foreign Key
    student = models.ForeignKey(Student,  on_delete=models.CASCADE) #Foreign Key


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    Course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    marks = models.IntegerField()
    is_pass = models.BooleanField()


class AdminSection(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,null=True, blank=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100, null=True, blank=True)