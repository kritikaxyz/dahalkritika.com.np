from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Notice, Event

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'important')
    list_filter = ('important', 'created_at')
    search_fields = ('title', 'content')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_upcoming')
    list_filter = ('start_date',)
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('is_upcoming',)

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)

# Register your models here.
