# views.py
import base64
import cv2
import numpy as np
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Attendance, CustomUser, StudentImage

def match_faces(image1_path, image2):
    """Compare two images using OpenCV for face matching."""
    img1 = cv2.imread(image1_path)
    img2 = cv2.imdecode(np.frombuffer(image2, np.uint8), cv2.IMREAD_COLOR)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces1 = face_cascade.detectMultiScale(img1, scaleFactor=1.1, minNeighbors=5)
    faces2 = face_cascade.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=5)

    return len(faces1) > 0 and len(faces2) > 0  # Return true if faces match

def markattendance_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        captured_image_data = request.POST.get('captured_image')

        try:
            # Decode Base64 image data
            _, image_data = captured_image_data.split(',')
            image_bytes = base64.b64decode(image_data)

            # Get student and their registered image
            student = CustomUser.objects.get(user_id=user_id, is_student=True)
            student_image = StudentImage.objects.get(student=student)

            # Compare faces
            image_path = settings.MEDIA_ROOT / student_image.image.name
            if match_faces(str(image_path), image_bytes):
                Attendance.objects.create(student=student, status=True, date=now())
                messages.success(request, f"Attendance marked for {student.username}.")
                return redirect('attendance_success')
            else:
                messages.error(request, "Face not matched. Please try again.")
        except CustomUser.DoesNotExist:
            messages.error(request, "Student not found.")
        except StudentImage.DoesNotExist:
            messages.error(request, "No registered photo for this student.")

    return render(request, 'attendance/attendance.html')



def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')