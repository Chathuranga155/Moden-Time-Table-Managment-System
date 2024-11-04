from django.urls import path
from . import views

urlpatterns = [
    # path('test_calendar_view/', views.test_calendar_view, name='test_calendar_view'),
    path('t_calendar_view/', views.t_calendar_view, name='t_calendar_view'),  
    # path('calendar_view/', views.calendar_view, name='calendar_view'),  
    path('all_events/', views.all_events, name='all_events'),

    # path('all_events/', views.all_events, name='all_events'),
    # path('add_event/', views.add_event, name='add_event'),
    # path('update_event/', views.update_event, name='update_event'),
    # path('remove_event/', views.remove_event, name='remove_event'),
    # path('calendar/', views.calendar_view, name='calendar_view'),
    # path('event/<int:event_id>/', views.view_event, name='view_event'),
 


    # path('calendar/', views.calendar_view, name='calendar_view'),
    # path('events/', views.get_events, name='get_events'),
    # path('event/add/', views.add_event, name='add_event'),
    # path('event/<int:event_id>/', views.view_event, name='view_event'),


    
]
