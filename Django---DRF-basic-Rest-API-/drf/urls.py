
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('employee/', include('employee.urls')),
]
