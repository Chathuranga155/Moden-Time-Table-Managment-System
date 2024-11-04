from django.urls import path
from . import views

urlpatterns = [
    path('main_list/', views.main_list, name='main_list'),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('exam_list/', views.exam_list, name='exam_list'),
    path('create_course/', views.create_course, name='create_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('create_faculty/', views.create_faculty, name='create_faculty'),
    path('faculty_list/', views.faculty_list, name='faculty_list'),
    path('create_room/', views.create_room, name='create_room'),
    path('room_list/', views.room_list, name='room_list'),
]
