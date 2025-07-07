"""
URL configuration for educore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', include('customadmin.urls', namespace='customadmin')),
    path('', include('courses.urls')),
    path('about/', views.about_view, name='about'),
    path('downloads/', views.downloads_view, name='downloads'),
    path('teachers-staff/', views.teachers_staff_view, name='teachers_staff'),
    path('executive-message/', views.executive_message_view, name='executive_message'),
    path('notices/', views.resources_view, name='notices'),
    path('contact/', views.contact_view, name='contact'),
    path('gallery/', views.gallery_view, name='gallery'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
