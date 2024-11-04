from django import forms
from .models import TeacherEvents, Batch, Degree

class TeacherEventForm(forms.ModelForm):
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), empty_label="Select Batch")
    degree = forms.ModelChoiceField(queryset=Degree.objects.all(), empty_label="Select Degree")

    class Meta:
        model = TeacherEvents
        fields = ['name', 'start', 'end', 'description', 'batch', 'degree', 'url', 'color']
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'color': forms.TextInput(attrs={'type': 'color'}),
        }
