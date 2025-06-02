# DjangoApis Project

This project is a Django-based REST API for managing company-related data. It is structured as a Django project named `companyapi` with an `api` app that contains the main business logic, models, serializers, and views.

## Project Structure

```
DjangoApis/
└── companyapi/
    ├── db.sqlite3                # SQLite database file
    ├── manage.py                 # Django management script
    ├── api/                      # Main app for API logic
    │   ├── models.py             # Database models
    │   ├── serializers.py        # Serializers for API
    │   ├── views.py              # API views
    │   ├── urls.py               # API URL routes
    │   ├── admin.py              # Admin site configuration
    │   ├── tests.py              # Unit tests
    │   └── migrations/           # Database migrations
    └── companyapi/               # Project settings
        ├── settings.py           # Django settings
        ├── urls.py               # Project URL routes
        ├── wsgi.py               # WSGI entry point
        └── asgi.py               # ASGI entry point
```

## Requirements
- Python 3.8+
- Django (recommended: latest stable version)

## Setup Instructions

1. **Clone the repository** (if not already):
   ```powershell
   git clone <your-repo-url>
   cd DjangoApis/companyapi
   ```

2. **Create a virtual environment (optional but recommended):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install django
   ```

4. **Apply migrations:**
   ```powershell
   python manage.py migrate
   ```

5. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

6. **Create a superuser (optional, for admin access):**
   ```powershell
   python manage.py createsuperuser
   ```

## Usage
- Access the API endpoints as defined in `api/urls.py`.
- Use the Django admin at `http://127.0.0.1:8000/admin/` to manage data if you created a superuser.

## Testing
To run tests:
```powershell
python manage.py test
```

## Notes
- Modify `api/models.py` to change or add database models.
- Update `api/serializers.py` and `api/views.py` to adjust API logic.
- All configuration is in `companyapi/settings.py`.

---
For more information, see the [Django documentation](https://docs.djangoproject.com/).
