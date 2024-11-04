# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# attendance/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=10, unique=True)
    is_student = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='attendance_customuser_set',  # Add related_name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='attendance_customuser_permissions_set',  # Add related_name to avoid conflict
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.user_id})"


class Attendance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    status = models.BooleanField(default=False)  # True = Present, False = Absent

    def __str__(self):
        return f"Attendance: {self.student.username} on {self.date}"


class StudentImage(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return f"Image for {self.student.username}"


