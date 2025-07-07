from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Notice, Event, AdvNotice, Download, Staff, ExecutiveMessage, GalleryImage, Facility

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'important')
    list_filter = ('important', 'created_at')
    search_fields = ('title', 'content')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_upcoming')
    list_filter = ('start_date',)
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('is_upcoming',)

class AdvNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'nepali_date', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('title', 'content', 'nepali_date')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'designation')
    list_filter = ('type',)
    search_fields = ('name', 'designation')

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(AdvNotice, AdvNoticeAdmin)
admin.site.register(Download)
admin.site.register(Staff, StaffAdmin)
admin.site.register(ExecutiveMessage)
admin.site.register(GalleryImage)
admin.site.register(Facility)

# Register your models here.
