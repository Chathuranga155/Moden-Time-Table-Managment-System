

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@sltc.ac.lk', 'required': 'required'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': 'required'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )





    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2']




from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'start', 'end', 'description', 'url', 'color']
        widgets = {
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'color': forms.TextInput(attrs={'type': 'color'})
        }








from django import forms
from .models import Teacher

class TeacherProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your username',
            'required': 'required'
        })
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your first name',
            'required': 'required'
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your last name',
            'required': 'required'
        })
    )

    department = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your department',
            'required': 'required'
        })
    )

    qualification = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your qualification',
            'required': 'required'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your email address',
            'required': 'required'
        })
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your phone number'
            
        })
    )

    birthday = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'MM/DD/YYYY'
            
        })
    )

    profile_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control-file btn-btn-primary'
            
        })
    )

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'department', 'qualification', 'email', 'phone', 'birthday', 'profile_image']

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if not profile_image:
            raise forms.ValidationError("At least one profile image must be uploaded.")
        return profile_image


from django import forms
from .models import Student

class StudentProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your first name',
            'required': 'required'
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your last name',
            'required': 'required'
        })
    )

    department = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your department'
        }),
        required=False
    )

    degree = forms.CharField(  # Updated from qualification to degree
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your degree'
        }),
        required=False
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your email address',
            'required': 'required'
        })
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your phone number'
        })
    )

    birthday = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'MM/DD/YYYY'
        }),
        required=False
    )

    profile_image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }),
        required=False  # Keep optional since it's null=True, blank=True in the model
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your address'
        }),
        required=False
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'department', 'address', 'degree', 'email', 'phone', 'birthday', 'profile_image']

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if not profile_image and self.instance.pk is None:  # Check for new instance
            raise forms.ValidationError("Please upload a profile image.")
        return profile_image





from .models import Dash_events

class Dash_eventsProfileForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your title',
            'required': 'required'
        })
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your description',
            'required': 'required'
        })
    )

    url = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your url'
        }),
        required=False
    )

    TYPE_CHOICES = [
        ('one_on_one', 'One On One'),
        ('group', 'Group')
    ]
    Type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Select Type'
        }),
        required=True
    )

    start = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'eventStart',
            'name': 'start',
            'placeholder': 'Oct. 12, 2024, 9:07 a.m.',
            'type': 'datetime-local'
        }),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True
    )

    end = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'eventEnd',
            'name': 'end',
            'placeholder': 'Oct. 12, 2024, 10:07 a.m.',
            'type': 'datetime-local'
        }),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True
    )

    color = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color',
            'id': 'eventColor',
            'name': 'color',
            'value': '#ff0000',
            'placeholder': 'Pick a color'
        }),
        required=False
    )




    class Meta:
        model = Dash_events
        fields = ['title', 'description', 'url', 'Type', 'start', 'end', 'color']





# Teacher events

from .models import Teacher_events           


class TeacherEventsProfileForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the title',
            'required': 'required'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={  # Changed to Textarea for better UX
            'class': 'form-control',
            'placeholder': 'Enter the description',
            'required': 'required'
        })
    )
    url = forms.URLField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a valid URL'
        }),
        required=False
    )

    TYPE_CHOICES = [
        ('one_on_one', 'One On One'),
        ('group', 'Group')
    ]
    type = forms.ChoiceField(  # Field name changed to match the model
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    start = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    end = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    color = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color'
        }),
        required=False
    )

    class Meta:
        model = Teacher_events  # Adjusted the model name
        fields = ['title', 'description', 'url', 'type', 'start', 'end', 'color']





