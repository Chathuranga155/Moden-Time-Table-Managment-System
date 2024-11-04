from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TeacherEvents
from .forms import TeacherEventForm

# def create_teacher_event(request):
#     if request.method == 'POST':
#         form = TeacherEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('create_teacher_event')  # Adjust if needed
#     else:
#         form = TeacherEventForm()

#     return render(request, 'test_create_event.html', {'form': form})

# def all_events(request):
#     events = TeacherEvents.objects.all().values(
#         'id', 'name', 'start', 'end', 'description', 'batch', 'degree', 'url', 'color'
#     )
#     return JsonResponse(list(events), safe=False)

# @csrf_exempt
# def add_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents(
#             name=data['name'],
#             start=data['start'],
#             end=data['end'],
#             description=data['description'],
#             batch=data['batch'],
#             degree=data['degree'],
#             url=data['url'],
#             color=data['color']
#         )
#         event.save()
#         return JsonResponse({"status": "success", "message": "Event added successfully."})

# @csrf_exempt
# def update_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents.objects.get(id=data['id'])
#         event.start = data['start']
#         event.end = data['end']
#         event.save()
#         return JsonResponse({"status": "success", "message": "Event updated successfully."})

# @csrf_exempt
# def remove_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents.objects.get(id=data['id'])
#         event.delete()
#         return JsonResponse({"status": "success", "message": "Event removed successfully."})






# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import JsonResponse
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import TeacherEvents
# from .forms import TeacherEventForm

# def create_teacher_event(request):
#     if request.method == 'POST':
#         form = TeacherEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('create_teacher_event')
#     else:
#         form = TeacherEventForm()

#     return render(request, 'test_create_event.html', {'form': form})

# def all_events(request):
#     events = TeacherEvents.objects.all().values(
#         'id', 'name', 'start', 'end', 'description', 'batch', 'degree', 'url', 'color'
#     )
#     return JsonResponse(list(events), safe=False)

# @csrf_exempt
# def add_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents(
#             name=data['name'],
#             start=data['start'],
#             end=data['end'],
#             description=data['description'],
#             batch_id=data['batch'],
#             degree_id=data['degree'],
#             url=data['url'],
#             color=data['color']
#         )
#         event.save()
#         return JsonResponse({"status": "success", "message": "Event added successfully."})

# @csrf_exempt
# def update_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents.objects.get(id=data['id'])
#         event.start = data['start']
#         event.end = data['end']
#         event.save()
#         return JsonResponse({"status": "success", "message": "Event updated successfully."})

# @csrf_exempt
# def remove_event(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         event = TeacherEvents.objects.get(id=data['id'])
#         event.delete()
#         return JsonResponse({"status": "success", "message": "Event removed successfully."})

# def calendar_view(request):
#     form = TeacherEventForm()
#     events = TeacherEvents.objects.all()
#     return render(request, 'teacher-calendar.html', {'form': form, 'events': events})

# def get_events(request):
#     events = TeacherEvents.objects.all()
#     events_data = []
#     for event in events:
#         events_data.append({
#             'title': event.name,
#             'start': event.start.isoformat(),
#             'end': event.end.isoformat(),
#             'description': event.description,
#             'batch': event.batch.batch_name,
#             'degree': event.degree.degree_name,
#             'color': event.color,
#             'url': reverse('view_event', args=[event.id])
#         })
#     return JsonResponse(events_data, safe=False)

# def view_event(request, event_id):
#     event = get_object_or_404(TeacherEvents, id=event_id)
#     return render(request, 'event_detail.html', {'event': event})





#      ----------------------------------------------------------------




from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json



from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import TeacherEvents
from .forms import TeacherEventForm


# def test_calendar_view(request):
#     return render(request, 'test_create_event.html')





# # def test_all_event(request):
# #     form = EventForm()  # Form for creating an event
# #     events = Events.objects.all()  # Fetch all events
# #     return render(request, 'users/test_all_event.html', {'form': form, 'events': events})

# def t_calendar_view(request):
#     form = TeacherEventForm()  # Form for creating an event
#     events = TeacherEvents.objects.all()  # Fetch all events
#     return render(request, 'teacher-calendar.html', {'form': form, 'events': events})


# def add_event(request):
#     if request.method == 'POST':
#         form = TeacherEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors})

# def get_events(request):
#     events = TeacherEvents.objects.all()
#     events_data = []
#     for event in events:
#         events_data.append({
            
#              'title': event.name,
#              'start': event.start.isoformat(),
#              'end': event.end.isoformat(),
#              'description': event.description,
#              'batch': event.batch.batch_name,
#              'degree': event.degree.degree_name,
#              'color': event.color,
#              'url': reverse('view_event', args=[event.id])
#         })
#     return JsonResponse(events_data, safe=False)

# def view_event(request, event_id):
#     event = get_object_or_404(TeacherEvents, id=event_id)
#     return render(request, 'event_detail.html', {'event': event})











from .models import TeacherEvents
from django.views.decorators.csrf import csrf_exempt
import json




def t_calendar_view(request):
    return render(request, 'teacher-calendar.html')

def all_events(request):
    events = TeacherEvents.objects.all()
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
        event = TeacherEvents(
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
        event = TeacherEvents.objects.get(id=data['id'])
        event.start = data['start']
        event.end = data['end']
        event.save()
        return JsonResponse({"status": "success", "message": "Event updated successfully."})

@csrf_exempt
def remove_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = TeacherEvents.objects.get(id=data['id'])
        event.delete()
        return JsonResponse({"status": "success", "message": "Event removed successfully."})



def all_events(request):
    # Retrieve events and map them to the correct format
    events = TeacherEvents.objects.all().values('name', 'start', 'end', 'description', 'url', 'color')
    events_list = list(events)  # Convert QuerySet to list
    return JsonResponse(events_list, safe=False)






# def all_events(request):
#     # Retrieve events and map them to the correct format
#     events = TeacherEvents.objects.all().values('id', 'name', 'start', 'end', 'description', 'batch', 'degree', 'url', 'color')
#     events_list = list(events)  # Convert QuerySet to list
#     return JsonResponse(events_list, safe=False)



















#      ----------------------------------------------------------------