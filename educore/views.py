from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from courses.models import AdvNotice, Download, ExecutiveMessage, GalleryImage, Staff
from django.core.exceptions import ValidationError
from PIL import Image

def about_view(request):
    """View function for the About Us page"""
    return render(request, 'about.html')

def resources_view(request):
    """View function for the Resources page"""
    return render(request, 'resources.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Form validation
        if not all([name, email, subject, message]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('contact')

        # Create email message
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # In production, uncomment this to send actual emails
            # send_mail(
            #     f'Contact Form: {subject}',
            #     email_message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [settings.CONTACT_EMAIL],
            #     fail_silently=False,
            # )

            # For development purposes, just log the message
            print(f"\n--- Contact Form Submission ---\nSubject: {subject}\n{email_message}\n---\n")

            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('contact')

    return render(request, 'contact_form.html')

def gallery_view(request):
    gallery_images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'gallery_images': gallery_images})

def downloads_view(request):
    downloads = Download.objects.all().order_by('-created_at')
    return render(request, 'downloads.html', {'downloads': downloads})

def teachers_staff_view(request):
    teachers_staff = Staff.objects.all().order_by('name')
    return render(request, 'teachers_staff.html', {'teachers_staff': teachers_staff})

def executive_message_view(request):
    executive_messages = ExecutiveMessage.objects.all().order_by('designation')
    return render(request, 'executive_message.html', {'executive_messages': executive_messages})

def ads_notice_context(request):
    ads_notices = AdvNotice.objects.filter(active=True, image__isnull=False).order_by('-created_at')
    return {'ads_notices': ads_notices}
