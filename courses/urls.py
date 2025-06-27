from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('notices/', views.notice_list, name='notice_list'),
    path('events/', views.event_list, name='event_list'),
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll'),
    path('enroll/confirm/<int:course_id>/', views.enroll_course, name='enroll_confirm'),
    path('courses/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
] 