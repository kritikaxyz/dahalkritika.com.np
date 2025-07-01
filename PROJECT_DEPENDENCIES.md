# Project Dependencies - EWSP Django Project

## Core Dependencies

### Django Framework
- **Django 5.0.6** - Main web framework
  - Provides MVC architecture
  - Built-in admin interface
  - ORM for database operations
  - Template system
  - URL routing

### Authentication & User Management
- **django-allauth** - Advanced authentication system
  - Social authentication support
  - Email verification
  - Account management
  - Custom user registration/login

### Database
- **SQLite3** - Default database (development)
  - File-based database
  - No additional installation required
  - Suitable for development and small projects

## Project Structure Dependencies

### Static Files
- **CSS Files**:
  - `style.css` - Main stylesheet
  - `navbar.css` - Navigation styling
  - `login-signup.css` - Authentication forms
  - `notices-events.css` - Content pages
  - `contact.css` - Contact form styling

- **JavaScript Files**:
  - `main.js` - Core functionality
  - `notices-events.js` - Dynamic content handling

- **Images**:
  - Hero images for different sections
  - Placeholder images
  - Pattern graphics

### Templates
- **Base Template**: `base.html` - Layout foundation
- **Account Templates**: Custom AllAuth templates
- **Content Templates**: Course, event, notice pages
- **Feature Templates**: Gallery, contact, about pages

## Development Dependencies

### Virtual Environment
- **Python venv** - Isolated Python environment
- **pip** - Package manager

### Development Tools
- **Django Debug Toolbar** (recommended for development)
- **Django Extensions** (optional for enhanced development)

## Configuration Dependencies

### Settings Configuration
```python
# Required Django Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth", 
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    
    # Third Party
    "allauth",
    "allauth.account", 
    "allauth.socialaccount",
    
    # Local Apps
    "courses.apps.CoursesConfig",
    "users.apps.UsersConfig",
]
```

### Middleware
```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware", 
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]
```

## Installation Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

## Production Considerations

### Recommended Production Dependencies
- **PostgreSQL** - Production database
- **Gunicorn** - WSGI server
- **Nginx** - Web server
- **Redis** - Caching and sessions
- **Whitenoise** - Static file serving

### Security Dependencies
- **django-cors-headers** - CORS handling
- **django-ratelimit** - Rate limiting
- **django-secure** - Security headers

## Environment Variables

### Required Environment Variables
```bash
SECRET_KEY=your-secret-key-here
DEBUG=False  # Production
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:pass@host:port/db
```

### Optional Environment Variables
```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Version Compatibility

### Python Version
- **Python 3.8+** (recommended 3.11+)

### Django Version
- **Django 5.0.6** (current)
- Compatible with Python 3.10+

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design for mobile devices

## Maintenance

### Regular Updates
- Keep Django updated for security patches
- Update dependencies regularly
- Monitor for deprecated packages

### Backup Strategy
- Database backups
- Static files backup
- Media files backup
- Code version control (Git)

This dependency structure ensures a robust, scalable, and maintainable Django application with modern web development practices. 