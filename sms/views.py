
from functools import partial
import this
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
#         'message': 'Department Data Fatched',
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
#                 'message' : "Add Department Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
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
#                 'message' : "Add Department Choice Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_department(request):
#     try:
#         data = request.data 
#         print(data.get('department_id'))
#         if not data.get('department_id'):
#             return Response({
#                 'status': False,
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Department.objects.get(department_id = data.get('department_id'))
#         serializer = DepartmentSerializer(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
#         'data':{}
#     })



# @api_view(['GET'])

# def get_students(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)

#     return Response({
#         'status': True,
#         'message': 'Students Data Fatched',
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
#                 'message' : "Add Student Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_student(request):
#     try:
#         data = request.data 
#         print(data.get('student_id'))
#         if not data.get('student_id'):
#             return Response({
#                 'status': False,
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
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
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
#         'data':{}
#     })


# Student API (GET, POST, PUT, DELETE)
class StudentAPI(APIView):

    def get(self,request):
        
        student_objs = Student.objects.filter(is_active=True).values() #active student
        serializer = StudentSerializer(student_objs, many = True)

        return Response({
            'status': True,
            'message': 'Active Students Data Fatched',
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
                'message' : "Add Student Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })
        



    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        obj = Student.objects.get(id = data.get('id')) #id-logic
        serializer = Student(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response({
                'status':True,
                'message' : "Data Update Success ",
                'data':serializer.data
            })
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def delete(self,request):
        
        data = request.data 
        print(data.get('student_id'))
        if not data.get('student_id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        obj = Student.objects.get(student_id = data.get('student_id'))
        serializer = Student(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.delete()
            return Response({
                'status':True,
                'message' : "Data Delete Successful ",
                'data':serializer.data
            })
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

# Parent API (GET, POST)
class ParentAPI(APIView):
    
    def get(self,request):
        parent_objs = Parent.objects.all()
        serializer = ParentSerializer(parent_objs, many = True)

        return Response({
            'status': True,
            'message': 'Parent Data Fatched',
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
                'message' : "Add Parent Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Parent.objects.filter(id=data.get('id')).exists()

        if is_exist:
            obj = Parent.objects.get(id = data.get('id'))
            serializer = ParentSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })
    
# Teacher API (GET, POST)
class TeacherAPI(APIView):
    
    def get(self,request):
        teacher_objs = Teacher.objects.filter(is_active=True).values()
        serializer = TeacherSerializer(teacher_objs, many = True)

        return Response({
            'status': True,
            'message': 'Teacher Data Fatched',
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
                'message' : "Add Teacher Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })

        is_exist = Teacher.objects.filter(id=data.get('id')).exists()
  

        if is_exist:
            obj = Teacher.objects.get(id = data.get('id'))
            serializer = TeacherSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

# Classroom API (GET, POST)
class ClassroomAPI(APIView):
    
    def get(self,request):
        classroom_objs = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom_objs, many = True)

        return Response({
            'status': True,
            'message': 'Classroom Data Fatched',
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
                'message' : "Add Classroom Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Classroom.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Classroom.objects.get(id = data.get('id'))
            serializer = ClassroomSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

# Grade API (GET, POST)
class GradeAPI(APIView):
    
    def get(self,request):
        grade_objs = Grade.objects.all()
        serializer = GradeSerializer(grade_objs, many = True)

        return Response({
            'status': True,
            'message': 'Grade Data Fatched',
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
                'message' : "Add Grade Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Grade.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Grade.objects.get(id = data.get('id'))
            serializer = GradeSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })
            


# Attendance API (GET, POST)
class AttendanceAPI(APIView):
    
    def get(self,request):
        attendance_objs = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance_objs, many = True)

        return Response({
            'status': True,
            'message': 'Attendance Data Fatched',
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
                'message' : "Add Attendance Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Attendance.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Attendance.objects.get(id = data.get('id'))
            serializer = AttendanceSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })


# ClassroomStudent API (GET, POST)
class ClassroomStudentAPI(APIView):
    
    def get(self,request):
        classroomstudent_objs = ClassroomStudent.objects.all()
        serializer = ClassroomStudentSerializer(classroomstudent_objs, many = True)

        return Response({
            'status': True,
            'message': 'ClassroomStudent Data Fatched',
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
                'message' : "Add ClassroomStudent Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = ClassroomStudent.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = ClassroomStudent.objects.get(id = data.get('id'))
            serializer = ClassroomStudentSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

# ExamType API (GET, POST)
class ExamTypeAPI(APIView):
    
    def get(self,request):
        examtype_objs = ExamType.objects.all()
        serializer = ExamTypeSerializer(examtype_objs, many = True)

        return Response({
            'status': True,
            'message': 'ExamType Data Fatched',
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
                'message' : "Add ExamType Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = ExamType.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = ExamType.objects.get(id = data.get('id'))
            serializer = ExamTypeSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

# Course API (GET, POST)
class CourseAPI(APIView):
    
    def get(self,request):
        course_objs = Course.objects.all()
        serializer = CourseSerializer(course_objs, many = True)

        return Response({
            'status': True,
            'message': 'Course Data Fatched',
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
                'message' : "Add Course Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Course.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Course.objects.get(id = data.get('id'))
            serializer = CourseSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

#  Exam API (GET, POST)
class ExamAPI(APIView):
    
    def get(self,request):
        exam_objs = Exam.objects.all()
        serializer = ExamSerializer(exam_objs, many = True)

        return Response({
            'status': True,
            'message': 'Exam Data Fatched',
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
                'message' : "Add Exam Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Exam.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Exam.objects.get(id = data.get('id'))
            serializer = ExamSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

#  Subject API (GET, POST)
class SubjectAPI(APIView):
    
    def get(self,request):
        subject_objs = Subject.objects.all()
        serializer = SubjectSerializer(subject_objs, many = True)

        return Response({
            'status': True,
            'message': 'Subject Data Fatched',
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
                'message' : "Add Subject Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })

    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = Subject.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = Subject.objects.get(id = data.get('id'))
            serializer = SubjectSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })


#  ExamResult API (GET, POST)
class ExamResultAPI(APIView):
    
    def get(self,request):
        examresult_objs = ExamResult.objects.all()
        serializer = ExamResultSerializer(examresult_objs, many = True)

        return Response({
            'status': True,
            'message': 'ExamResult Data Fatched',
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
                'message' : "Add ExamResult Successful ",
                'data':serializer.data
            })

        print(data)
        return Response({
            'status':False,
            'message' : "Fields Invalid Data ",
            'data':serializer.errors
        })
    def put(self,request):
        
        data = request.data 
        print(data.get('id')) #url params
        if not data.get('id'):
            return Response({
                'status': False,
                'message':'ID is required',
                'data' : {}
            })
        print(data.get('id'))

        is_exist = ExamResult.objects.filter(id=data.get('id')).exists()
        print(is_exist)

        if is_exist:
            obj = ExamResult.objects.get(id = data.get('id'))
            serializer = ExamResultSerializer(obj,  data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response({
                    'status':True,
                    'message' : "Data Update Success ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        else:
            return Response({
                'status':False,
                'message':"This ID is not available"
            })

#  AdminSection API (GET)
class AdminSectionAPI(APIView):
    
    def get(self,request):
        adminsection_objs = AdminSection.objects.all()
        serializer = AdminSectionSerializer(adminsection_objs, many = True)

        return Response({
            'status': True,
            'message': 'AdminSection Data Fatched',
            'data': serializer.data
        })
         