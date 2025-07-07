from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='notice_attachments/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    registration_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.title

    @property
    def is_upcoming(self):
        if self.start_date is None:
            return False
        return self.start_date > timezone.now()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()
    video_url = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=50)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

class AdvNotice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='advnotice_images/', blank=True, null=True)  # noqa: spellchecker:disable
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nepali_date = models.CharField(max_length=20, blank=True, help_text='Date in Nepali calendar (e.g., 2081-03-15)')
    active = models.BooleanField(default=True, help_text='Show this notice in the modal if active')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Advertisement/Notice'
        verbose_name_plural = 'Advertisements/Notices'

    def __str__(self):
        return self.title

class Download(models.Model):
    CATEGORY_CHOICES = [
        ('forms', 'Forms'),
        ('documents', 'Documents'),
        ('brochures', 'Brochures'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='downloads/')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    download_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Staff(models.Model):
    STAFF_TYPE_CHOICES = [
        ("teaching", "Teaching Staff"),
        ("non_teaching", "Non-Teaching Staff"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES, default="teaching")
    designation = models.CharField(max_length=100, blank=True, null=True)  # Subject or Role
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.name}"

class ExecutiveMessage(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='executive_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.designation} - {self.name}"

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('activities', 'Activities'),
        ('facilities', 'Facilities'),
        ('students', 'Students'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class Facility(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='facility_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.name
