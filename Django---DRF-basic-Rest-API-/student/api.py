from django.http import QueryDict
from rest_framework import generics
from rest_framework.response import Response
from .serializer import StudentSerializer,LoginSerializer
from .models import Student
from rest_framework import  serializers
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        data = request.POST.copy()  # Create a mutable copy of the POST data
        password = data.get('password')
        data['password'] = make_password(password)  # Import make_password from django.contrib.auth.hashers

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()

        refresh = RefreshToken.for_user(student)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(token)
    


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_email = serializer.validated_data['student_email']
        password = serializer.validated_data['password']

        try:
            student = Student.objects.get(student_email=student_email)
        except Student.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=400)

        if not check_password(password, student.password):
            return Response({'error': 'Invalid email or password.'}, status=400)

        refresh = RefreshToken.for_user(student)
        response_data = {
            'email': student_email,
            'access_token': str(refresh.access_token),
        }
        return Response(response_data)
