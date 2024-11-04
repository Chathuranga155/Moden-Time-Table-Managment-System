# # urls.py

from django.contrib.auth import views as auth_views
from .views import register, CustomLoginView, dashboard  #CustomLoginView_T, CustomLoginView_s
from . import views


from django.urls import path
from .views import CustomLoginView, register, dashboard, index


from django.conf import settings
from django.conf.urls.static import static

# project/urls.py
from django.conf.urls import handler404
from schedule.views import custom_404_view

handler404 = custom_404_view






urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    
    # Login Views
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('teacherlogin/', views.TeacherLoginView.as_view(), name='teacherlogin'),

    # Dashboard Views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    # Logout Views
    path('teacher_logout/', views.teacher_logout, name='teacher_logout'),
    path('student_logout/', views.student_logout, name='student_logout'),




    path('intergration/', views.intergration, name='intergration'),  #intergration  
     path('s_intergration/', views.s_intergration, name='s_intergration'),  #intergration  

    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),   #privacy_policy
    path('terms_service/', views.terms_service, name='terms_service'),   #terms_service   techer-profile
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),   #  teacher_profile    
    path('student_profile/', views.student_profile, name='student_profile'),   #  student_profile    

    # path('create_teacher_event/', views.create_teacher_event, name='create_teacher_event'),     #create_teacher_event





    # path('calendar/', views.calendar_view, name='calendar'),
    # path('get-all-events/', views.get_all_events, name='get_all_events'),
    # path('add-event/', views.add_event, name='add_event'),
    # path('update-event/', views.update_event, name='update_event'),
    # path('delete-event/', views.delete_event, name='delete_event'),

    # path('calendar/', views.calendar_view, name='calendar'),
    # path('add-event/', views.add_event, name='add_event'),
    # path('get-events/', views.get_events, name='get_events'),
    # path('event/<int:event_id>/', views.view_event, name='view_event'),


    path('calendar/', views.calendar_view, name='calendar_view'), 
    path('s_calendar_view/', views.s_calendar_view, name='s_calendar_view'), 
    path('t_calendar_view/', views.t_calendar_view, name='t_calendar_view'),   #teacher calender
 
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('remove_event/', views.remove_event, name='remove_event'),
    path('all_events/', views.all_events, name='all_events'),



    path('page_eventadd/', views.page_eventadd, name='page_eventadd'),   #page events adding  
    path('s_event_list/', views.s_event_list, name='s_event_list'),   #page events adding  
    path('t_page_eventadd/', views.t_page_eventadd, name='t_page_eventadd'),   #t_page_eventadd
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),  #t_page_eventadd
    # path('t_calendar_view/', views.t_calendar_view, name='t_calendar_view'),  #t_page_eventadd
    path('groups/', views.Groups, name='groups'),   #page groups   

    path('calendar_connections/', views.calendar_connections, name='calendar_connections'),   #page groups     

 

    # path('test_all_event/', views.test_all_event, name='test_all_event'), 



 

  


]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)









