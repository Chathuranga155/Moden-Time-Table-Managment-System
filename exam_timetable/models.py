from django.db import models

# Define the Student model
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Define the Faculty model
class Faculty(models.Model):
    faculty_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Define the Course model
class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.course_name

# Define the Exam model
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(help_text="Exam duration in hours")
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course.course_name} Exam on {self.date}"

# Define the Room model
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_name
