# Django v0.9

A Django project with blog content management and member profile system.

## Features

- **Core App**: Blog post and category management with admin interface
- **Medlemmer App**: Member list and profile editing system
- Responsive UI with modern styling
- User authentication and permissions

## Quick Start

1. Activate virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies (if needed):
   ```powershell
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```powershell
   python manage.py migrate
   ```

4. Create superuser for admin access:
   ```powershell
   python manage.py createsuperuser
   ```

5. Populate test member data (optional):
   ```powershell
   python manage.py populate_members
   ```

6. Start development server:
   ```powershell
   python manage.py runserver
   ```

## URLs

- **Admin Panel**: http://localhost:8000/admin/
- **Member List**: http://localhost:8000/medlemmer/
- **Member Detail**: http://localhost:8000/medlemmer/<id>/
- **Edit Profile**: http://localhost:8000/medlemmer/edit/

## Version History

### v0.9 (Current)
- Initial Django setup
- Core app with Post and Category models
- Medlemmer app with user profiles
- Member list and edit functionality
- Admin interface for content management
- Test data with 5 sample members

## Requirements

- Python 3.14+
- Django 6.0.3
