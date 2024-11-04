from django import forms
from .models import Exam, Course, Room, Faculty, Student

# Form to create and schedule an Exam
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['course', 'date', 'time', 'duration', 'room']

# Form to create a Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'faculty', 'students']

# Form to add Faculty
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'email']

# Form to add Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email']

# Form to add a Room
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'capacity']
