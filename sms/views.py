from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
# from yaml import serializer
from .serializer import DepartmentSerializer, DepartmentChoiceSerializer, StudentSerializer
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
        try:
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
        except Exception as e:
            print(e)



    def patch(self,request):
        try:
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
                    'msg' : "Success Data ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'msg' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'msg' : "Invalid ID",
            'data':{}
        })
    
    def delete(self,request):
        try:
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
                    'msg' : "Success Data ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'msg' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'msg' : "Invalid ID",
            'data':{}
        })


class DepartmentAPI(APIView):
    def get(self, request):
        department_objs = Department.objects.all()
        serializer = DepartmentSerializer(department_objs, many = True)

        return Response({
            'status': True,
            'msg': 'Department Data Fatched',
            'data': serializer.data
        }) 

    def post(self, request):
        try:
            data = request.data 
            serializer = DepartmentSerializer(data = data)
            if serializer.is_valid():
                serializer.save
                print(serializer.data)
                return Response({
                    'status':True,
                    'msg' : "Add Department Successful ",
                    'data':serializer.data
                })

            print(data)
            return Response({
            '   status':False,
                'msg' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'msg' : "Something Went Wrong",
        })

    def patch(self,request):
        try:
            data = request.data 
            print(data.get('department_id'))
            if not data.get('department_id'):
                return Response({
                    'status': False,
                    'msg':'ID is required',
                    'data' : {}
                })
            obj = Department.objects.get(department_id = data.get('department_id'))
            serializer = DepartmentSerializer(obj, data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'msg' : "Success Data ",
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'msg' : "Fields Invalid Data ",
                'data':serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'msg' : "Invalid ID",
            'data':{}
        })
