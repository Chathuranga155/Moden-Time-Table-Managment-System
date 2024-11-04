# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.markattendance_view, name='attendance'),
    path('attendance/success/', views.attendance_success, name='attendance_success'),
]
