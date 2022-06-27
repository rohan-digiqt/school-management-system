
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Parent(models.Model):
    # parent_id = models.IntegerField(primary_key=True)
    parent_email = models.EmailField()
    parent_password = models.CharField(max_length=20)
    parent_fname = models.CharField(max_length=20)
    parent_lname = models.CharField(max_length=20)
    parent_date_of_birth = models.DateField()
    parent_mobile_no = models.IntegerField()
    parent_status = models.BooleanField(default=False)


class Teacher(models.Model):
    # teacher_id = models.IntegerField(primary_key=True)
    teacher_email = models.EmailField()
    teacher_password = models.CharField(max_length=20)
    teacher_fname = models.CharField(max_length=20)
    teacher_lname = models.CharField(max_length=20)
    teacher_date_of_birth = models.DateField()
    teacher_mobile_no = models.IntegerField()
    teacher_status = models.BooleanField(default=False)

class Classroom(models.Model):
    # classroom_id = models.IntegerField(primary_key=True)
    classroom_year = models.CharField(max_length=20)
    classroom_section = models.CharField(max_length=20)
    classroom_status = models.BooleanField()
    classroom_remarks = models.TextField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key



class Grade(models.Model):
    grade_id = models.IntegerField(primary_key=True)
    grade_name = models.CharField(max_length=10)

class Cource(models.Model):
    # cource_id = models.IntegerField(primary_key=True)
    cource_name = models.CharField(max_length=20)
    cource_description = models.TextField()

class Student(models.Model):
    # student_id = models.IntegerField(primary_key=True)
    student_email = models.EmailField(max_length=254)
    student_password = models.CharField(max_length=20)
    student_fname = models.CharField(max_length=10)
    student_lname = models.CharField(max_length=10)
    student_date_of_birth = models.DateField()
    student_mobile_no = models.IntegerField()
    parent_id = models.ForeignKey(Parent, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    student_date_of_join = models.DateField() #joining date
    student_status = models.BooleanField(default=False) #is_active



class Attendance(models.Model):
    attendance_date = models.DateField()
    student_id = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    attendance_status = models.BooleanField(default=False)
    attendance_remarks = models.TextField()

class Classroom_Student(models.Model):
    # classroom_student_id = models.IntegerField(primary_key=True, default=True)
    classroom_id = models.ForeignKey(Classroom, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    student_id = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key


class Exam_Type(models.Model):
    # exam_type_id = models.IntegerField(primary_key=True)
    exam_type_name = models.CharField(max_length=15)
    exam_type_description = models.TextField()

class Exam(models.Model):
    # exam_id = modedls.IntegerField(primary_key=True)
    exam_type_id = models.ForeignKey(Exam_Type, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key

class Exam_Result(models.Model):
    exam_id = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    student_id = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    cource_id = models.ForeignKey(Cource, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    exam_result_marks = models.IntegerField()
    exam_result_status = models.BooleanField()

class Department(models.Model):
    # department_id = models.IntegerField(primary_key=True)
    DEPARTMENT_CHOICE = (
        ('Computer','Computer'),
        ('It','It'),
        ('Mechanical','Mechanical'),
        ('Civil','Civil'),
        ('Electrical','Electrical')
    )
    department_name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICE)

