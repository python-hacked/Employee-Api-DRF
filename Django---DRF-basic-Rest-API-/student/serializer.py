from rest_framework import  serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        
class LoginSerializer(serializers.Serializer):
    student_email = serializers.EmailField()
    password = serializers.CharField()