from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Category, Lesson, Enrollment, Notice, Event, AdvNotice, Staff
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone

def get_ads_notice():
    return AdvNotice.objects.filter(active=True, image__isnull=False).order_by('-created_at').first()

def home(request):
    courses = Course.objects.filter(is_published=True)
    categories = Category.objects.all()
    ads_notice = get_ads_notice()
    context = {
        'courses': courses,
        'categories': categories,
        'ads_notice': ads_notice,
    }
    return render(request, 'courses/home.html', context)

def course_list(request):
    courses = Course.objects.filter(is_published=True)
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if category_id:
        courses = courses.filter(category_id=category_id)

    context = {
        'courses': courses,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    }
    return render(request, 'courses/course_list.html', context)

def notice_list(request):
    notices_list = Notice.objects.all()
    # Pagination
    paginator = Paginator(notices_list, 10)  # Show 10 notices per page
    page_number = request.GET.get('page')
    notices = paginator.get_page(page_number)
    return render(request, 'courses/notice_list.html', {'notices': notices})

def event_list(request):
    # Get past events
    past_events = Event.objects.filter(end_date__lt=timezone.now()).order_by('-start_date')
    # Get upcoming events
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')
    context = {
        'past_events': past_events,
        'upcoming_events': upcoming_events
    }
    return render(request, 'courses/event_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_published=True)
    lessons = course.lessons.all()
    is_enrolled = False

    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()

    context = {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk, is_published=True)

    if request.method == 'POST':
        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )
        if created:
            messages.success(request, f'Successfully enrolled in {course.title}')
        else:
            messages.info(request, f'You are already enrolled in {course.title}')
        return redirect('course_detail', pk=pk)

    return render(request, 'courses/enroll_confirm.html', {'course': course})

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    context = {
        'enrollments': enrollments,
    }
    return render(request, 'courses/my_courses.html', context)

def teachers_staff_view(request):
    teachers_staff = Staff.objects.all()
    return render(request, 'teachers_staff.html', {'teachers_staff': teachers_staff})
