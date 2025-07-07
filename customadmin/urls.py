from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'customadmin'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # User Management
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    
    # Notice Management
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/create/', views.notice_create, name='notice_create'),
    path('notices/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notices/<int:notice_id>/edit/', views.notice_edit, name='notice_edit'),
    path('notices/<int:notice_id>/delete/', views.notice_delete, name='notice_delete'),
    
    # Event Management
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    
    # Course Management
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    
    # Staff Management
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:staff_id>/', views.staff_detail, name='staff_detail'),
    path('staff/<int:staff_id>/edit/', views.staff_edit, name='staff_edit'),
    path('staff/<int:staff_id>/delete/', views.staff_delete, name='staff_delete'),
    
    # AdvNotice Management
    path('advnotices/', views.advnotice_list, name='advnotice_list'),
    path('advnotices/create/', views.advnotice_create, name='advnotice_create'),
    path('advnotices/<int:advnotice_id>/', views.advnotice_detail, name='advnotice_detail'),
    path('advnotices/<int:advnotice_id>/edit/', views.advnotice_edit, name='advnotice_edit'),
    path('advnotices/<int:advnotice_id>/delete/', views.advnotice_delete, name='advnotice_delete'),
    
    # Download Management
    path('downloads/', views.download_list, name='download_list'),
    path('downloads/create/', views.download_create, name='download_create'),
    path('downloads/<int:download_id>/', views.download_detail, name='download_detail'),
    path('downloads/<int:download_id>/edit/', views.download_edit, name='download_edit'),
    path('downloads/<int:download_id>/delete/', views.download_delete, name='download_delete'),
    
    # Executive Message Management
    path('executives/', views.executive_list, name='executive_list'),
    path('executives/create/', views.executive_create, name='executive_create'),
    path('executives/<int:executive_id>/', views.executive_detail, name='executive_detail'),
    path('executives/<int:executive_id>/edit/', views.executive_edit, name='executive_edit'),
    path('executives/<int:executive_id>/delete/', views.executive_delete, name='executive_delete'),
    
    # Gallery Management
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('gallery/<int:gallery_id>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:gallery_id>/delete/', views.gallery_delete, name='gallery_delete'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='customadmin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='customadmin:login'), name='logout'),
] 