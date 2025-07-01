# Django Project Structure - EWSP (Educational Website)

## Project Overview
This is a Django-based educational website project with a clean, modern design using white and blue color scheme.

## Project Root: `/Users/dipan/Desktop/ewsp`

### Main Django Project: `educore/`
- **Settings**: `educore/settings.py` - Main Django configuration
- **URLs**: `educore/urls.py` - Root URL configuration
- **WSGI**: `educore/wsgi.py` - WSGI application entry point
- **ASGI**: `educore/asgi.py` - ASGI application entry point

### Installed Django Apps

#### 1. Django Built-in Apps
```python
INSTALLED_APPS = [
    "django.contrib.admin",        # Django admin interface
    "django.contrib.auth",         # Authentication system
    "django.contrib.contenttypes", # Content type framework
    "django.contrib.sessions",     # Session framework
    "django.contrib.messages",     # Messaging framework
    "django.contrib.staticfiles",  # Static file handling
    "django.contrib.sites",        # Site framework
]
```

#### 2. Third-Party Apps
```python
# Authentication & User Management
"allauth",                    # AllAuth authentication
"allauth.account",           # AllAuth account management
"allauth.socialaccount",     # AllAuth social authentication
```

#### 3. Local Apps
```python
# Custom Applications
"courses.apps.CoursesConfig",  # Courses, notices, and events management
"users.apps.UsersConfig",      # Custom user management
```

### App Details

#### `courses/` App
- **Purpose**: Manages courses, notices, and events
- **Models**: 
  - `Notice` - For announcements and notices
  - `Event` - For upcoming events
- **Views**: Handles course-related pages and functionality
- **URLs**: `courses/urls.py` - Course-specific URL patterns
- **Templates**: Course-related templates in `templates/courses/`

#### `users/` App
- **Purpose**: Custom user management and authentication
- **Models**: Custom user models if any
- **Views**: User-related views and functionality
- **URLs**: `users/urls.py` - User-specific URL patterns

### Static Files Structure
```
static/
├── css/
│   ├── contact.css
│   ├── login-signup.css
│   ├── navbar.css
│   ├── notices-events.css
│   └── style.css
├── images/
│   ├── about-hero.jpg
│   ├── event-header.jpg
│   ├── event-placeholder.jpg
│   ├── notice-header.jpg
│   ├── pattern.svg
│   └── resources-hero.jpg
└── js/
    ├── main.js
    └── notices-events.js
```

### Templates Structure
```
templates/
├── account/              # AllAuth templates (login, signup)
│   ├── login.html
│   └── signup.html
├── courses/              # Course-related templates
│   ├── event_list.html
│   ├── home.html
│   └── notice_list.html
├── base.html             # Base template
├── about.html
├── contact_form.html
├── downloads.html
├── executive_message.html
├── gallery.html
├── notification_banner.html
├── resources.html
└── teachers_staff.html
```

### Key Configuration

#### Database
- **Engine**: SQLite3 (development)
- **File**: `db.sqlite3` in project root

#### Static Files
- **Static URL**: `/static/`
- **Static Root**: `staticfiles/`
- **Media URL**: `/media/`
- **Media Root**: `media/`

#### Authentication
- **Backend**: Django AllAuth
- **Login Redirect**: `home`
- **Logout Redirect**: `home`
- **Email Verification**: Mandatory

#### Color Scheme
- **Primary**: Blue (#007bff)
- **Background**: White (#fff)
- **Consistent**: White and blue theme throughout

### Development Setup
1. **Virtual Environment**: `venv/`
2. **Requirements**: `requirements.txt`
3. **Django Management**: `manage.py`

### Key Features
- Modern responsive design
- User authentication with AllAuth
- Course and event management
- Notice system
- Gallery functionality
- Contact forms
- Executive messaging
- Teacher and staff information
- Resource downloads

### URL Structure
- **Home**: `/` - Main landing page
- **Courses**: `/courses/` - Course listings
- **Events**: `/events/` - Event listings
- **Notices**: `/notices/` - Notice listings
- **Gallery**: `/gallery/` - Image gallery
- **About**: `/about/` - About page with dropdown
- **Contact**: `/contact/` - Contact form
- **Resources**: `/resources/` - Resource downloads
- **Login/Signup**: `/accounts/login/`, `/accounts/signup/`

This project follows Django best practices with a clean separation of concerns, modular app structure, and modern web development standards. 