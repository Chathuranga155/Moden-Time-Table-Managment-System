# forms.py
from django import forms

class AttendanceForm(forms.Form):
    user_id = forms.CharField(max_length=10, label="Student ID")
    image = forms.ImageField(label="Upload Image")
