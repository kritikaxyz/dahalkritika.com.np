from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from courses.models import (
    Notice, Event, Category, Course, Lesson, Enrollment, 
    AdvNotice, Download, Staff, ExecutiveMessage, GalleryImage
)

# Create your views here.

@login_required
def dashboard(request):
    # Get counts for all models
    user_count = User.objects.count()
    notice_count = Notice.objects.count()
    event_count = Event.objects.count()
    course_count = Course.objects.count()
    staff_count = Staff.objects.count()
    adv_notice_count = AdvNotice.objects.count()
    download_count = Download.objects.count()
    executive_count = ExecutiveMessage.objects.count()
    gallery_count = GalleryImage.objects.count()
    
    context = {
        'user_count': user_count,
        'notice_count': notice_count,
        'event_count': event_count,
        'course_count': course_count,
        'staff_count': staff_count,
        'adv_notice_count': adv_notice_count,
        'download_count': download_count,
        'executive_count': executive_count,
        'gallery_count': gallery_count,
    }
    return render(request, 'customadmin/dashboard.html', context)

# User Management
@login_required
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/user_list.html', {'page_obj': page_obj})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'customadmin/user_detail.html', {'user': user})

# Notice Management
@login_required
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    paginator = Paginator(notices, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/notice_list.html', {'page_obj': page_obj})

@login_required
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'customadmin/notice_detail.html', {'notice': notice})

@login_required
def notice_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        important = request.POST.get('important') == 'on'
        attachment = request.FILES.get('attachment')
        
        notice = Notice.objects.create(
            title=title,
            content=content,
            important=important,
            attachment=attachment
        )
        messages.success(request, 'Notice created successfully!')
        return redirect('customadmin:notice_list')
    
    return render(request, 'customadmin/notice_form.html')

@login_required
def notice_edit(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == 'POST':
        notice.title = request.POST.get('title')
        notice.content = request.POST.get('content')
        notice.important = request.POST.get('important') == 'on'
        if 'attachment' in request.FILES:
            notice.attachment = request.FILES['attachment']
        notice.save()
        messages.success(request, 'Notice updated successfully!')
        return redirect('customadmin:notice_list')
    
    return render(request, 'customadmin/notice_form.html', {'notice': notice})

@login_required
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('customadmin:notice_list')
    return render(request, 'customadmin/notice_confirm_delete.html', {'notice': notice})

# Event Management
@login_required
def event_list(request):
    events = Event.objects.all().order_by('start_date')
    paginator = Paginator(events, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/event_list.html', {'page_obj': page_obj})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'customadmin/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == 'POST':
        event = Event.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date'),
            location=request.POST.get('location'),
            registration_url=request.POST.get('registration_url'),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Event created successfully!')
        return redirect('customadmin:event_list')
    
    return render(request, 'customadmin/event_form.html')

@login_required
def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.location = request.POST.get('location')
        event.registration_url = request.POST.get('registration_url')
        if 'image' in request.FILES:
            event.image = request.FILES['image']
        event.save()
        messages.success(request, 'Event updated successfully!')
        return redirect('customadmin:event_list')
    
    return render(request, 'customadmin/event_form.html', {'event': event})

@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('customadmin:event_list')
    return render(request, 'customadmin/event_confirm_delete.html', {'event': event})

# Course Management
@login_required
def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    paginator = Paginator(courses, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/course_list.html', {'page_obj': page_obj})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'customadmin/course_detail.html', {'course': course})

# Staff Management
@login_required
def staff_list(request):
    staff = Staff.objects.all().order_by('name')
    paginator = Paginator(staff, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/staff_list.html', {'page_obj': page_obj})

@login_required
def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    return render(request, 'customadmin/staff_detail.html', {'staff': staff})

@login_required
def staff_create(request):
    if request.method == 'POST':
        staff = Staff.objects.create(
            name=request.POST.get('name'),
            type=request.POST.get('type'),
            designation=request.POST.get('designation'),
            bio=request.POST.get('bio'),
            photo=request.FILES.get('photo')
        )
        messages.success(request, 'Staff member created successfully!')
        return redirect('customadmin:staff_list')
    
    return render(request, 'customadmin/staff_form.html')

@login_required
def staff_edit(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    if request.method == 'POST':
        staff.name = request.POST.get('name')
        staff.type = request.POST.get('type')
        staff.designation = request.POST.get('designation')
        staff.bio = request.POST.get('bio')
        if 'photo' in request.FILES:
            staff.photo = request.FILES['photo']
        staff.save()
        messages.success(request, 'Staff member updated successfully!')
        return redirect('customadmin:staff_list')
    
    return render(request, 'customadmin/staff_form.html', {'staff': staff})

@login_required
def staff_delete(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    if request.method == 'POST':
        staff.delete()
        messages.success(request, 'Staff member deleted successfully!')
        return redirect('customadmin:staff_list')
    return render(request, 'customadmin/staff_confirm_delete.html', {'staff': staff})

# AdvNotice Management
@login_required
def advnotice_list(request):
    advnotices = AdvNotice.objects.all().order_by('-created_at')
    paginator = Paginator(advnotices, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/advnotice_list.html', {'page_obj': page_obj})

@login_required
def advnotice_detail(request, advnotice_id):
    advnotice = get_object_or_404(AdvNotice, pk=advnotice_id)
    return render(request, 'customadmin/advnotice_detail.html', {'advnotice': advnotice})

@login_required
def advnotice_create(request):
    if request.method == 'POST':
        advnotice = AdvNotice.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            nepali_date=request.POST.get('nepali_date'),
            active=request.POST.get('active') == 'on',
            image=request.FILES.get('image')
        )
        messages.success(request, 'Advertisement/Notice created successfully!')
        return redirect('customadmin:advnotice_list')
    
    return render(request, 'customadmin/advnotice_form.html')

@login_required
def advnotice_edit(request, advnotice_id):
    advnotice = get_object_or_404(AdvNotice, pk=advnotice_id)
    if request.method == 'POST':
        advnotice.title = request.POST.get('title')
        advnotice.content = request.POST.get('content')
        advnotice.nepali_date = request.POST.get('nepali_date')
        advnotice.active = request.POST.get('active') == 'on'
        if 'image' in request.FILES:
            advnotice.image = request.FILES['image']
        advnotice.save()
        messages.success(request, 'Advertisement/Notice updated successfully!')
        return redirect('customadmin:advnotice_list')
    
    return render(request, 'customadmin/advnotice_form.html', {'advnotice': advnotice})

@login_required
def advnotice_delete(request, advnotice_id):
    advnotice = get_object_or_404(AdvNotice, pk=advnotice_id)
    if request.method == 'POST':
        advnotice.delete()
        messages.success(request, 'Advertisement/Notice deleted successfully!')
        return redirect('customadmin:advnotice_list')
    return render(request, 'customadmin/advnotice_confirm_delete.html', {'advnotice': advnotice})

# Download Management
@login_required
def download_list(request):
    downloads = Download.objects.all().order_by('-uploaded_at')
    paginator = Paginator(downloads, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/download_list.html', {'page_obj': page_obj})

@login_required
def download_detail(request, download_id):
    download = get_object_or_404(Download, pk=download_id)
    return render(request, 'customadmin/download_detail.html', {'download': download})

@login_required
def download_create(request):
    if request.method == 'POST':
        download = Download.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            is_active=request.POST.get('is_active') == 'on',
            download_count=int(request.POST.get('download_count', 0)),
            file=request.FILES.get('file')
        )
        messages.success(request, 'Download created successfully!')
        return redirect('customadmin:download_list')
    
    return render(request, 'customadmin/download_form.html')

@login_required
def download_edit(request, download_id):
    download = get_object_or_404(Download, pk=download_id)
    if request.method == 'POST':
        download.title = request.POST.get('title')
        download.description = request.POST.get('description')
        download.category = request.POST.get('category')
        download.is_active = request.POST.get('is_active') == 'on'
        download.download_count = int(request.POST.get('download_count', 0))
        if 'file' in request.FILES:
            download.file = request.FILES['file']
        download.save()
        messages.success(request, 'Download updated successfully!')
        return redirect('customadmin:download_list')
    
    return render(request, 'customadmin/download_form.html', {'download': download})

@login_required
def download_delete(request, download_id):
    download = get_object_or_404(Download, pk=download_id)
    if request.method == 'POST':
        download.delete()
        messages.success(request, 'Download deleted successfully!')
        return redirect('customadmin:download_list')
    return render(request, 'customadmin/download_confirm_delete.html', {'download': download})

# Executive Message Management
@login_required
def executive_list(request):
    executives = ExecutiveMessage.objects.all().order_by('-created_at')
    paginator = Paginator(executives, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/executive_list.html', {'page_obj': page_obj})

@login_required
def executive_detail(request, executive_id):
    executive = get_object_or_404(ExecutiveMessage, pk=executive_id)
    return render(request, 'customadmin/executive_detail.html', {'executive': executive})

@login_required
def executive_create(request):
    if request.method == 'POST':
        executive = ExecutiveMessage.objects.create(
            name=request.POST.get('name'),
            designation=request.POST.get('designation'),
            message=request.POST.get('message'),
            is_active=request.POST.get('is_active') == 'on',
            image=request.FILES.get('image')
        )
        messages.success(request, 'Executive message created successfully!')
        return redirect('customadmin:executive_list')
    
    return render(request, 'customadmin/executive_form.html')

@login_required
def executive_edit(request, executive_id):
    executive = get_object_or_404(ExecutiveMessage, pk=executive_id)
    if request.method == 'POST':
        executive.name = request.POST.get('name')
        executive.designation = request.POST.get('designation')
        executive.message = request.POST.get('message')
        executive.is_active = request.POST.get('is_active') == 'on'
        if 'image' in request.FILES:
            executive.image = request.FILES['image']
        executive.save()
        messages.success(request, 'Executive message updated successfully!')
        return redirect('customadmin:executive_list')
    
    return render(request, 'customadmin/executive_form.html', {'executive': executive})

@login_required
def executive_delete(request, executive_id):
    executive = get_object_or_404(ExecutiveMessage, pk=executive_id)
    if request.method == 'POST':
        executive.delete()
        messages.success(request, 'Executive message deleted successfully!')
        return redirect('customadmin:executive_list')
    return render(request, 'customadmin/executive_confirm_delete.html', {'executive': executive})

# Gallery Management
@login_required
def gallery_list(request):
    gallery = GalleryImage.objects.all().order_by('-created_at')
    paginator = Paginator(gallery, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customadmin/gallery_list.html', {'page_obj': page_obj})

@login_required
def gallery_detail(request, gallery_id):
    gallery = get_object_or_404(GalleryImage, pk=gallery_id)
    return render(request, 'customadmin/gallery_detail.html', {'gallery': gallery})

@login_required
def gallery_create(request):
    if request.method == 'POST':
        gallery = GalleryImage.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            is_active=request.POST.get('is_active') == 'on',
            order=int(request.POST.get('order', 0)),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Gallery image created successfully!')
        return redirect('customadmin:gallery_list')
    
    return render(request, 'customadmin/gallery_form.html')

@login_required
def gallery_edit(request, gallery_id):
    gallery = get_object_or_404(GalleryImage, pk=gallery_id)
    if request.method == 'POST':
        gallery.title = request.POST.get('title')
        gallery.description = request.POST.get('description')
        gallery.category = request.POST.get('category')
        gallery.is_active = request.POST.get('is_active') == 'on'
        gallery.order = int(request.POST.get('order', 0))
        if 'image' in request.FILES:
            gallery.image = request.FILES['image']
        gallery.save()
        messages.success(request, 'Gallery image updated successfully!')
        return redirect('customadmin:gallery_list')
    
    return render(request, 'customadmin/gallery_form.html', {'gallery': gallery})

@login_required
def gallery_delete(request, gallery_id):
    gallery = get_object_or_404(GalleryImage, pk=gallery_id)
    if request.method == 'POST':
        gallery.delete()
        messages.success(request, 'Gallery image deleted successfully!')
        return redirect('customadmin:gallery_list')
    return render(request, 'customadmin/gallery_confirm_delete.html', {'gallery': gallery})
