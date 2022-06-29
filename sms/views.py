
from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
# from yaml import serializer
from .serializer import *
from .models import *


# Create your views here.

# @api_view(['GET'])

# def get_department(request):
#     department_objs = Department.objects.all()
#     serializer = DepartmentSerializer(department_objs, many = True)

#     return Response({
#         'status': True,
#         'msg': 'Department Data Fatched',
#         'data': serializer.data
#     }) 



# @api_view(['POST'])
# def post_department(request):
#     try:
#         data = request.data 
#         serializer = DepartmentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'msg' : "Add Department Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Something Went Wrong",
#     })

# @api_view(['POST'])
# def post_department_choice(request):
#     try:
#         data = request.data 
#         serializer = DepartmentChoiceSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'msg' : "Add Department Choice Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_department(request):
#     try:
#         data = request.data 
#         print(data.get('department_id'))
#         if not data.get('department_id'):
#             return Response({
#                 'status': False,
#                 'msg':'ID is required',
#                 'data' : {}
#             })
#         obj = Department.objects.get(department_id = data.get('department_id'))
#         serializer = DepartmentSerializer(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'msg' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Invalid ID",
#         'data':{}
#     })



# @api_view(['GET'])

# def get_students(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)

#     return Response({
#         'status': True,
#         'msg': 'Students Data Fatched',
#         'data': serializer.data
#     }) 

# @api_view(['POST'])
# def post_student(request):
#     try:
#         data = request.data 
#         serializer = StudentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'msg' : "Add Student Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_student(request):
#     try:
#         data = request.data 
#         print(data.get('student_id'))
#         if not data.get('student_id'):
#             return Response({
#                 'status': False,
#                 'msg':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'msg' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Invalid ID",
#         'data':{}
#     })

# @api_view(['DELETE'])

# def delete_student(request):
#     try:
#         data = request.data 
#         print(data.get('student_id'))
#         if not data.get('student_id'):
#             return Response({
#                 'status': False,
#                 'msg':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response({
#                 'status':True,
#                 'msg' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'msg' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'msg' : "Invalid ID",
#         'data':{}
#     })


# Student API (GET, POST, PATCH, DELETE)
class StudentAPI(APIView):

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Students Data Fatched',
            'data': serializer.data
        }) 
    
    def post(self,request):
        
        data = request.data 
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Student Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })
        



    def patch(self,request):
        
        data = request.data 
        print(data.get('student_id'))
        if not data.get('student_id'):
            return Response({
                'status': False,
                'msg':'ID is required',
                'data' : {}
            })
        obj = Student.objects.get(student_id = data.get('student_id'))
        serializer = Student(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                    'msg' : "Data Update Success ",
                    'data':serializer.data
                })
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def delete(self,request):
        
        data = request.data 
        print(data.get('student_id'))
        if not data.get('student_id'):
            return Response({
                'status': False,
                'msg':'ID is required',
                'data' : {}
            })
        obj = Student.objects.get(student_id = data.get('student_id'))
        serializer = Student(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.delete()
            return Response({
                'status':True,
                'msg' : "Data Delete Successful ",
                'data':serializer.data
            })
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Parent API (GET, POST)
class ParentAPI(APIView):
    
    def get(self,request):
        parent_objs = Parent.objects.all()
        serializer = ParentSerializer(parent_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Parent Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ParentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Parent Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })
    
# Teacher API (GET, POST)
class TeacherAPI(APIView):
    
    def get(self,request):
        teacher_objs = Teacher.objects.all()
        serializer = TeacherSerializer(teacher_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Teacher Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = TeacherSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Teacher Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Teacher API (GET, POST)
class ClassroomAPI(APIView):
    
    def get(self,request):
        classroom_objs = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Classroom Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ClassroomSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Classroom Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Grade API (GET, POST)
class GradeAPI(APIView):
    
    def get(self,request):
        grade_objs = Grade.objects.all()
        serializer = GradeSerializer(grade_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Grade Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = GradeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Grade Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Attendance API (GET, POST)
class AttendanceAPI(APIView):
    
    def get(self,request):
        attendance_objs = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Attendance Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = AttendanceSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Attendance Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })


# ClassroomStudent API (GET, POST)
class ClassroomStudentAPI(APIView):
    
    def get(self,request):
        classroomstudent_objs = ClassroomStudent.objects.all()
        serializer = ClassroomStudentSerializer(classroomstudent_objs, many = True)

        return Response({
            'status': True,
            'msg': 'ClassroomStudent Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ClassroomStudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add ClassroomStudent Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })


# ExamType API (GET, POST)
class ExamTypeAPI(APIView):
    
    def get(self,request):
        examtype_objs = ExamType.objects.all()
        serializer = ExamTypeSerializer(examtype_objs, many = True)

        return Response({
            'status': True,
            'msg': 'ExamType Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ExamTypeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add ExamType Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Course API (GET, POST)
class CourseAPI(APIView):
    
    def get(self,request):
        course_objs = Course.objects.all()
        serializer = CourseSerializer(course_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Course Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = CourseSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Course Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

#  Exam API (GET, POST)
class ExamAPI(APIView):
    
    def get(self,request):
        exam_objs = Exam.objects.all()
        serializer = ExamSerializer(exam_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Exam Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ExamSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Exam Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

#  Subject API (GET, POST)
class SubjectAPI(APIView):
    
    def get(self,request):
        subject_objs = Subject.objects.all()
        serializer = SubjectSerializer(subject_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Subject Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = SubjectSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add Subject Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })


#  ExamResult API (GET, POST)
class ExamResultAPI(APIView):
    
    def get(self,request):
        examresult_objs = ExamResult.objects.all()
        serializer = ExamResultSerializer(examresult_objs, many = True)

        return Response({
            'status': True,
            'msg': 'ExamResult Data Fatched',
            'data': serializer.data
        }) 
    def post(self,request):
        
        data = request.data 
        serializer = ExamResultSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'msg' : "Add ExamResult Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'msg' : "Fields Invalid Data ",
            'data':serializer.errors
        })

#  AdminSection API (GET)
class AdminSectionAPI(APIView):
    
    def get(self,request):
        adminsection_objs = AdminSection.objects.all()
        serializer = AdminSectionSerializer(adminsection_objs, many = True)

        return Response({
            'status': True,
            'msg': 'AdminSection Data Fatched',
            'data': serializer.data
        }) 