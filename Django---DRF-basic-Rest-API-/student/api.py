from rest_framework import generics
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()

        refresh = RefreshToken.for_user(student)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(token)
    
class LoginAPIView(TokenObtainPairView):
    serializer_class = StudentSerializer    