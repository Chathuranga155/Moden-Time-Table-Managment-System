# admin.py
from django.contrib import admin
from .models import CustomUser, Attendance, StudentImage

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id', 'is_student')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')


@admin.register(StudentImage)
class StudentImageAdmin(admin.ModelAdmin):
    list_display = ('student', 'image')
