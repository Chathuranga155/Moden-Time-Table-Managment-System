from django.contrib import admin
from .models import Student, Faculty, Course, Exam, Room

# Register the Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email')
    search_fields = ('student_id', 'name', 'email')

admin.site.register(Student, StudentAdmin)

# Register the Faculty model
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'name', 'email')
    search_fields = ('faculty_id', 'name', 'email')

admin.site.register(Faculty, FacultyAdmin)

# Register the Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'faculty')
    search_fields = ('course_code', 'course_name')
    list_filter = ('faculty',)

admin.site.register(Course, CourseAdmin)

# Register the Exam model
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'time', 'duration', 'room')
    search_fields = ('course__course_name', 'room')
    list_filter = ('date', 'room')

admin.site.register(Exam, ExamAdmin)

# Register the Room model
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'capacity')
    search_fields = ('room_name',)
    list_filter = ('capacity',)

admin.site.register(Room, RoomAdmin)
