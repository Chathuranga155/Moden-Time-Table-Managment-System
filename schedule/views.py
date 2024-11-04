from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Use the custom user model


"""
-----------------------------------------
# User Registration View
-----------------------------------------
"""

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in upon registration
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


"""
-----------------------------------------
# Custom Login Views for Role-based Redirection
-----------------------------------------
"""

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_redirect_url(self):
        """Redirect users based on their roles."""
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'student':
                return reverse_lazy('student_dashboard')
            elif user.role == 'teacher':
                return reverse_lazy('teacher_dashboard')
        return reverse_lazy('dashboard')  # Default redirection


class TeacherLoginView(LoginView):
    template_name = 'users/teacher_login.html'

    def get_redirect_url(self):
        """Ensure teachers are redirected properly."""
        if self.request.user.is_authenticated and self.request.user.role == 'teacher':
            return reverse_lazy('teacher_dashboard')
        return reverse_lazy('teacherlogin')  # Default if not teacher


"""
-----------------------------------------
# Dashboard Views with Role-based Access
-----------------------------------------
"""

@login_required
def dashboard(request):
    """Handle general dashboard access based on user role."""
    if request.user.role == 'student':
        return redirect('student_dashboard')
    elif request.user.role == 'teacher':
        return redirect('teacher_dashboard')
    return render(request, 'default_dashboard.html')


@login_required(login_url='studentlogin')
def student_dashboard(request):
    """Display student-specific dashboard."""
    if request.user.role == 'student':
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'role': request.user.get_role_display()
        }
        return render(request, 'users/student_dashboard.html', context)
    return redirect('login')  # Redirect if not student


@login_required(login_url='teacherlogin')
def teacher_dashboard(request):
    """Display teacher-specific dashboard with user details."""
    if request.user.role == 'teacher':
        user_details = User.objects.all()  # Fetch all users
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'role': request.user.get_role_display(),
            'user_details': user_details
        }
        return render(request, 'teacher_dashboard.html', context)
    return redirect('teacherlogin')  # Redirect if not teacher


"""
-----------------------------------------
# Logout Views for Teachers and Students
-----------------------------------------
"""

def teacher_logout(request):
    """Log out the teacher."""
    logout(request)
    return redirect('teacherlogin')


def student_logout(request):
    """Log out the student."""
    logout(request)
    return redirect('login')






""" 
-----------------------------------------

# Index View

-----------------------------------------

"""




def index(request):
    myemployee = User.objects.all()  # Retrieve all users
    context = {"employee": myemployee}  # Pass data to the template
    return render(request, 'index.html', context=context)  # Render with correct context


def my_scedule(request):
    # Retrieve the logged-in user's schedule data and pass it to the template
    # user_schedule = request.user.schedule.all()
    # context = {'schedule': user_schedule}
    return render(request, 'my_schedule.html')












from django.http import JsonResponse

# from .models import Events

# # Calendar view
# def calendar_view(request):
#     all_events = Events.objects.all()
#     context = {
#         "events": all_events,
#     }
#     return render(request, 'calendar.html', context)

# # Get all events as JSON for FullCalendar
# def get_all_events(request):
#     all_events = Events.objects.all()
#     event_list = []
#     for event in all_events:
#         event_list.append({
#             'title': event.name,
#             'id': event.id,
#             'start': event.start.strftime("%Y-%m-%dT%H:%M:%S"),
#             'end': event.end.strftime("%Y-%m-%dT%H:%M:%S"),
#         })
#     return JsonResponse(event_list, safe=False)

# # Add new event via AJAX
# def add_event(request):
#     if request.method == 'GET':
#         start = request.GET.get('start')
#         end = request.GET.get('end')
#         name = request.GET.get('title')
#         event = Events(name=name, start=start, end=end)
#         event.save()
#         return JsonResponse({'success': True})

# # Update event via AJAX
# def update_event(request):
#     if request.method == 'GET':
#         event_id = request.GET.get('id')
#         start = request.GET.get('start')
#         end = request.GET.get('end')
#         name = request.GET.get('title')
#         event = Events.objects.get(id=event_id)
#         event.start = start
#         event.end = end
#         event.name = name
#         event.save()
#         return JsonResponse({'success': True})

# # Remove event via AJAX
# def delete_event(request):
#     if request.method == 'GET':
#         event_id = request.GET.get('id')
#         event = Events.objects.get(id=event_id)
#         event.delete()
#         return JsonResponse({'success': True})




# intergration


def intergration(request):
  
    return render(request, 'main-integration.html')  # Render with correct context



def s_intergration(request):
  
    return render(request, 'users/main-integration.html')  # Render with correct context



#privecy policy

def privacy_policy(request):
  
    return render(request, 'privacy-policy.html')  # Render with correct context


#terms-of-service.html


def terms_service(request):
  
    return render(request, 'terms-of-service.html')  # terms-of-service.html






"""

-------------------------------------------

teacher profile  start

-----------------------------------------


"""




#teacher profile


# def teacher_profile(request):
  
#     return render(request, 'techer-profile.html')  

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def teacher_profile(request):
    # Get the teacher instance based on the logged-in user
    teacher = get_object_or_404(Teacher, user=request.user)

    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES, instance=teacher)  # Bind the form with the teacher instance
        if form.is_valid():
            form.save()  # Save the updated instance
            messages.success(request, 'Profile updated successfully!')  # Add a success message
            return redirect('teacher_profile')  # Redirect to the same page to avoid resubmission
    else:
        form = TeacherProfileForm(instance=teacher)  # Populate the form with the current data

    context = {
        'form': form,
        'teacher': teacher,
    }
    return render(request, 'techer-profile.html', context)







# @login_required
# def teacher_profile(request):
#     # Attempt to get the teacher object
#     teacher = Teacher.objects.filter(user=request.user).first()

#     # If the teacher does not exist, handle the situation
#     if teacher is None:
#         # You can redirect to a create teacher profile page or render a message
#         return redirect('teacher_profile')  # Replace with your actual create profile URL

#     if request.method == 'POST':
#         form = TeacherProfileForm(request.POST, request.FILES, instance=teacher)  # Add request.FILES for file uploads
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_profile')
#     else:
#         form = TeacherProfileForm(instance=teacher)

#     context = {
#         'form': form,
#         'teacher': teacher,
#     }
#     return render(request, 'teacher-profile.html', context)


"""

-------------------------------------------

teacher profile  end

-----------------------------------------


"""




"""

-------------------------------------------

student profile  start

-----------------------------------------


"""




#student-profile.html


# def student_profile(request):
  
#     return render(request, 'student-profile.html')  



from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def student_profile(request):
    # Get the student instance based on the logged-in user
    student = get_object_or_404(Student, user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)  # Bind the form with the student instance
        if form.is_valid():
            form.save()  # Save the updated instance
            messages.success(request, 'Profile updated successfully!')  # Add a success message
            return redirect('student_profile')  # Redirect to the same page to avoid resubmission
    else:
        form = StudentProfileForm(instance=student)  # Populate the form with the current data

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'student-profile.html', context)




"""

-------------------------------------------

Student profile  end

-----------------------------------------


"""

#dashbord page event add

def page_eventadd(request):
  
    return render(request, 'users/page-add-event.html')  










from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Events
from .forms import EventForm
import json

def calendar_view(request):
    form = EventForm()  # Form for creating an event
    events = Events.objects.all()  # Fetch all events
    return render(request, 'calendar.html', {'form': form, 'events': events})



# def test_all_event(request):
#     form = EventForm()  # Form for creating an event
#     events = Events.objects.all()  # Fetch all events
#     return render(request, 'users/test_all_event.html', {'form': form, 'events': events})

def s_calendar_view(request):
    form = EventForm()  # Form for creating an event
    events = Events.objects.all()  # Fetch all events
    return render(request, 'users/calendar.html', {'form': form, 'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

def get_events(request):
    events = Events.objects.all()
    events_data = []
    for event in events:
        events_data.append({
            'title': event.name,
            'start': event.start.isoformat(),
            'end': event.end.isoformat(),
            'description': event.description,
            'color': event.color,
            'url': reverse('view_event', args=[event.id])  # To view full details
        })
    return JsonResponse(events_data, safe=False)

def view_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    return render(request, 'event_detail.html', {'event': event})











from .models import Events
from django.views.decorators.csrf import csrf_exempt
import json

def calendar_view(request):
    return render(request, 'calendar.html')

def all_events(request):
    events = Events.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'id': event.id,
            'title': event.name,
            'start': event.start.isoformat(),
            'end': event.end.isoformat(),
            'description': event.description,
            'url': event.url,
            'color': event.color
        })
    return JsonResponse(event_list, safe=False)

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Events(
            name=data['name'],
            start=data['start'],
            end=data['end'],
            description=data['description'],
            url=data['url'],
            color=data['color']
        )
        event.save()
        return JsonResponse({"status": "success", "message": "Event added successfully."})

@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Events.objects.get(id=data['id'])
        event.start = data['start']
        event.end = data['end']
        event.save()
        return JsonResponse({"status": "success", "message": "Event updated successfully."})

@csrf_exempt
def remove_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = Events.objects.get(id=data['id'])
        event.delete()
        return JsonResponse({"status": "success", "message": "Event removed successfully."})



def all_events(request):
    # Retrieve events and map them to the correct format
    events = Events.objects.all().values('name', 'start', 'end', 'description', 'url', 'color')
    events_list = list(events)  # Convert QuerySet to list
    return JsonResponse(events_list, safe=False)









 # Assuming you have an Event model

from .models import Events

# def test_all_event(request):
#     s_events = Events.objects.all()  # Fetch all events from the database
#     return render(request, 'users/test_all_event.html', {'s_events': s_events})



# main dash events


from django.shortcuts import render, get_object_or_404, redirect
from .models import Dash_events
from .forms import Dash_eventsProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# View for creating a new event
def page_eventadd(request):
    if request.method == 'POST':
        form = Dash_eventsProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to event list or any other page after successful submission
    else:
        form = Dash_eventsProfileForm()
    
    context = {
        'form': form
    }
    return render(request, 'users/page-add-event.html', context)

# View for updating an existing event
def update_event(request, event_id):
    event = get_object_or_404(Dash_events, id=event_id)
    
    if request.method == 'POST':
        form = Dash_eventsProfileForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('s_event_list')  # Redirect to event list or any other page after successful update
    else:
        form = Dash_eventsProfileForm(instance=event)
    
    context = {
        'form': form,
        'event': event
    }
    return render(request, 'users/update_event.html', context)

# View for listing all events
def s_event_list(request):
    events = Dash_events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'users/student_dashboard.html', context)






def Groups(request):
  
    return render(request, 'users/page-groups.html')  


#     page-calendar-connections   


def calendar_connections(request):
  
    return render(request, 'users/page-calendar-connections.html')  




# Teacher section









# main Teacher events



from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher_events
from .forms import TeacherEventsProfileForm





# Create event view
def t_page_eventadd(request):
    if request.method == 'POST':
        form = TeacherEventsProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('t_page_eventadd')  # Redirect to calendar view after saving
    else:
        form = TeacherEventsProfileForm()

    context = {'form': form}
    return render(request, 'teacher-add-event.html', context)

# Update event view
def update_event(request, event_id):
    event = get_object_or_404(Teacher_events, id=event_id)
    if request.method == 'POST':
        form = TeacherEventsProfileForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('t_page_eventadd')
    else:
        form = TeacherEventsProfileForm(instance=event)

    context = {'form': form, 'event': event}
    return render(request, 'update_event.html', context)

# View to display all events
def dashboard(request):
    t_events = Teacher_events.objects.all()
    print(t_events)  # Check if events are correctly retrieved
    context = {'t_events': t_events}
    return render(request, 'teacher_dashboard.html', context)






# Teacher Calender View Controller

def t_calendar_view(request):
  
    return render(request, 'teacher-calendar.html')  


# from .models import TeacherEvents
# from .forms import TeacherEventForm





# def create_teacher_event(request):
#     if request.method == 'POST':
#         form = TeacherEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('event_list')  # Adjust the redirect as needed
#     else:
#         form = TeacherEventForm()
    
#     return render(request, 'test_create_event.html', {'form': form})




#custom error page

# views.py
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500_view(request):
    return render(request, 'errors/500.html', status=500)
