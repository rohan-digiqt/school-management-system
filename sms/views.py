from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from .utils import *

'''Function Based API's'''

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
   


'''Class Based API's'''

# Student API (GET, POST, PUT, DELETE)
class StudentAPI(APIView):

    def get(self, request):
        data_obj=Student.objects.filter()
        return Response(create_response([obj.get_student_data() for obj in data_obj],True,"Success"))

    def post(self, request):
    
        serializer_instance = StudentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))

    def put(self, request):
    
        serializer_instance = StudentSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Student.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))



    def delete(self, request):

        serializer_instance = StudentSerializer(data=request.data)
        if not serializer_instance.get('student_id'):
            return Response(create_response(False, "ID not available", {}))

        obj = Student.objects.get(student_id=serializer_instance.get('student_id'))
        if serializer_instance.is_valid():
            serializer_instance.delete()
            return Response(create_response(serializer_instance.data, True,'Success'))
        return Response(create_response(serializer_instance.erroe, False,'Error'))

# Parent API (GET, POST)


class ParentAPI(APIView):

    def get(self, request):
        data_obj=Parent.objects.filter()
        return Response(create_response([obj.get_parent_data() for obj in data_obj],True,"Success"))

    def post(self, request):
    
        serializer_instance = ParentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))
        

    def put(self, request):
    
        serializer_instance = ParentSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Parent.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


# Teacher API (GET, POST)


class TeacherAPI(APIView):

    def get(self, request):
        data_obj=Teacher.objects.filter()
        return Response(create_response([obj.get_teacher_data() for obj in data_obj],True,"Success"))

    def post(self, request):
    
        serializer_instance = TeacherSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))

    def put(self, request):
    
        serializer_instance = TeacherSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Teacher.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


        
# Classroom API (GET, POST)


class ClassroomAPI(APIView):

    def get(self, request):
        data_obj=Classroom.objects.filter()
        return Response(create_response([obj.get_classroom_data() for obj in data_obj],True,"Success"))
    def get_req(model, srlz):
        obj = model.objects.all()
        serializer = srlz(obj, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        return Response(create_response(True, "Success", serializer.data))

    def post(self, request):
    
        serializer_instance = ClassroomSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))

    def put(self, request):
    
        serializer_instance = ClassroomSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Classroom.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))

# Grade API (GET, POST)


class GradeAPI(APIView):

    def get(self, request):
        data_obj=Grade.objects.filter()
        return Response(create_response([obj.get_grade_data() for obj in data_obj],True,"Success"))

    def post(self, request):

        serializer_instance = GradeSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))

    def put(self, request):

        serializer_instance = GradeSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Grade.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


            
        # return put_req(Grade, GradeSerializer, request)

# Attendance API (GET, POST)
class AttendanceAPI(APIView):

    def get(self, request):
        data_obj=Attendance.objects.filter()
        return Response(create_response([obj.get_attendance_data() for obj in data_obj],True,"Success"))

    def post(self, request):
    
        serializer_instance = AttendanceSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))

    def put(self, request):
    
        serializer_instance = AttendanceSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Attendance.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


# ClassroomStudent API (GET, POST)
class ClassroomStudentAPI(APIView):

    def get(self, request):
        data_obj=ClassroomStudent.objects.filter()
        return Response(create_response([obj.get_classroomstudent_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = ClassroomStudentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = ClassroomStudentSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = ClassroomStudent.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


# ExamType API (GET, POST)


class ExamTypeAPI(APIView):

    def get(self, request):
        data_obj=ExamType.objects.filter()
        return Response(create_response([obj.get_examtype_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = ExamTypeSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = ExamTypeSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = ExamType.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))

        

# Course API (GET, POST)


class CourseAPI(APIView):

    def get(self, request):
        data_obj=Course.objects.filter()
        return Response(create_response([obj.get_course_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = CourseSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = CourseSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Course.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


#  Exam API (GET, POST)


class ExamAPI(APIView):

    def get(self, request):
        data_obj=Exam.objects.filter()
        return Response(create_response([obj.get_exam_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = ExamSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = ExamSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Exam.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))

#  Subject API (GET, POST)


class SubjectAPI(APIView):

    def get(self, request):
        data_obj=Subject.objects.filter()
        return Response(create_response([obj.get_subject_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = SubjectSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = SubjectSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = Subject.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))

        

#  ExamResult API (GET, POST)
class ExamResultAPI(APIView):

    def get(self, request):
        data_obj=ExamResult.objects.filter()
        return Response(create_response([obj.get_examresult_data() for obj in data_obj],True,"Success"))

    def post(self, request):
        
        serializer_instance = ExamResultSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(create_response(serializer_instance.data,True,"Success"))
        return Response(create_response(serializer_instance.errors, False,"Invalid Data" ))


    def put(self, request):
    
        serializer_instance = ExamResultSerializer(data = request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False,'Invalid ID'))

        is_exist = ExamResult.objects.filter(id=request.data.get('id')).last() 

        if not is_exist:
            return Response(create_response(False, "ID not available", {}))
        else:
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(create_response(serializer_instance.data, True,'Success'))
            return Response(create_response(serializer_instance.erroe, False,'Error'))


#  AdminSection API (GET)


class AdminSectionAPI(APIView):

    def get(self, request):
        data_obj=AdminSection.objects.filter()
        return Response(create_response([obj.get_adminsection_data() for obj in data_obj],True,"Success"))
