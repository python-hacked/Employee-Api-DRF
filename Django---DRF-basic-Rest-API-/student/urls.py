from django.urls import path
from .api import StudentApi,RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('api',StudentApi.as_view()),
    path('api/register/', RegistrationAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),
]
