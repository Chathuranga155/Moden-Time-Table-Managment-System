from django import forms
from .models import Exam, Course, Room, Faculty, Student

# Form to create and schedule an Exam
class ExamForm(forms.ModelForm):
    course = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the course name',
            'required': 'required',
        })
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select the exam date',
            'type': 'date',  # Date picker
            'required': 'required',
        })
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the exam time',
            'type': 'time',  # Time picker
            'required': 'required',
        })
    )

    duration = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the exam duration (e.g., 2 hours)',
            'required': 'required',
        })
    )

    room = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the room count',
            'min': '1',  # Minimum number for room count
            'required': 'required',
        })
    )

    class Meta:
        model = Exam
        fields = ['course', 'date', 'time', 'duration', 'room']


# Form to create a Course
class CourseForm(forms.ModelForm):
    course_code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the course code',
            'required': 'required',
        })
    )
    course_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'course_name',
            'placeholder': 'Enter the course name',
            'required': 'required',
        })
    )

    
    # faculty = forms.Select(
    #     attrs={'class': 'form-control', 'required': 'required', 'style': 'color: blue; background-color: #f0f0f0; font-size: 14px;', }
    # )
    # students = forms.SelectMultiple(
    #     attrs={'class': 'form-control', 'size': '5', 'style': 'color: blue; background-color: #f0f0f0; font-size: 14px;',  }
    # )


     # Faculty dropdown
    faculty = forms.ModelChoiceField(
        queryset=Faculty.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control custom-select',  # Add a custom class
            'required': 'required',
        })
    )

    # Students multi-select
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control custom-multiselect',  # Add a custom class
            'size': '5',
        })
    )


    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'faculty', 'students', ]


# Form to add Faculty
class FacultyForm(forms.ModelForm):
    faculty_id = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the faculty ID',
            'required': 'required',
        })
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the faculty name',
            'required': 'required',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the faculty email',
            'required': 'required',
        })
    )

    class Meta:
        model = Faculty
        fields = ['faculty_id', 'name', 'email']


# Form to add Student
class StudentForm(forms.ModelForm):
    student_id = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the student ID',
            'required': 'required',
        })
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the student name',
            'required': 'required',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the student email',
            'required': 'required',
        })
    )

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email']


# Form to add a Room
class RoomForm(forms.ModelForm):
    room_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the room name',
            'required': 'required',
        })
    )
    capacity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the room capacity',
            'min': '1',
            'required': 'required',
        })
    )

    class Meta:
        model = Room
        fields = ['room_name', 'capacity']
