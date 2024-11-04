from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ExamForm, CourseForm, FacultyForm, StudentForm, RoomForm
from .models import Exam, Course, Faculty, Student, Room

# View to create a new exam
def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exam_timetable/create_exam.html', {'form': form})

# View to list all exams
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_timetable/exam_list.html', {'exams': exams})

# View to create a course
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'exam_timetable/create_course.html', {'form': form})

# View to list all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'exam_timetable/course_list.html', {'courses': courses})

# View to create a faculty member
def create_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'exam_timetable/create_faculty.html', {'form': form})

# View to list all faculty members
def faculty_list(request):
    faculty = Faculty.objects.all()
    return render(request, 'exam_timetable/faculty_list.html', {'faculty': faculty})

# View to create a room
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'exam_timetable/create_room.html', {'form': form})

# View to list all rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'exam_timetable/room_list.html', {'rooms': rooms})


def main_list(request):
  
    return render(request, 'exam_timetable/index.html')
