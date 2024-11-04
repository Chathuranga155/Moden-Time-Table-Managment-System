from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),  # Uncomment if you want to add Admin role
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    user_id = models.CharField(max_length=6, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id:
            current_year = timezone.now().year % 100
            sequence_number = CustomUser.objects.filter(user_id__startswith=str(current_year)).count() + 1
            self.user_id = f"{current_year:02d}{sequence_number:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    degree = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

# Events model
class Events(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    color = models.CharField(max_length=7, default='#000000')  # HEX color code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Calendar Event')
        verbose_name_plural = _('Calendar Events')

    def __str__(self):
        return self.name or 'Event'
    


class Dash_events(models.Model):
     
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True) 
    url = models.URLField(null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)  # Added max_length
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    color = models.CharField(max_length=7, default='#000000')  # HEX color code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or 'Dashevent'





# teacher events




class Teacher_events(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)  # Renamed to lowercase
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    color = models.CharField(max_length=7, default='#000000')  # HEX color code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or 'Teacher Event'



# teacher events for add event in calender event

 
