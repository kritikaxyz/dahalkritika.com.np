# Educational Website

A dynamic educational platform built with Django.

## Features
- User authentication and authorization
- Course management system
- Interactive learning materials
- Student progress tracking
- Responsive design
- Beautiful contact form with animations

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000 to see the website. 