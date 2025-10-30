# Password Manager Setup Instructions

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation Steps

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Features

### Security Features
- **Password Encryption**: All stored passwords are encrypted using Fernet symmetric encryption
- **User Authentication**: Secure login/logout system using Django's built-in authentication
- **User Isolation**: Each user can only access their own passwords

### Password Management
- **Add Passwords**: Store passwords with title, username, URL, notes, and category
- **View Passwords**: List all passwords with search and category filtering
- **Edit Passwords**: Update existing password entries
- **Delete Passwords**: Remove passwords with confirmation dialog
- **Password Generator**: Built-in secure password generator
- **Copy to Clipboard**: Easy copy functionality for usernames and passwords
- **Show/Hide Passwords**: Toggle password visibility

### User Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Bootstrap Styling**: Modern, clean interface
- **Dashboard**: Overview of recent passwords and quick actions
- **Search & Filter**: Find passwords quickly by title or category

## File Structure
```
PasswordManager/
├── manage.py
├── requirements.txt
├── db.sqlite3 (created after migrations)
└── PasswordManager/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    ├── models.py
    ├── forms.py
    ├── wsgi.py
    ├── asgi.py
    └── templates/
        ├── base.html
        ├── home.html
        ├── login.html
        ├── register.html
        ├── password_list.html
        ├── add_password.html
        ├── edit_password.html
        └── confirm_delete.html
```

## Usage Tips

1. **First Time Setup**: Create an account using the registration form
2. **Adding Passwords**: Use descriptive titles and categories for easy organization
3. **Security**: Use the password generator for strong, unique passwords
4. **Organization**: Categorize passwords (e.g., "Social Media", "Work", "Banking")
5. **Search**: Use the search feature to quickly find specific passwords

## Important Security Notes

- Keep your Django SECRET_KEY secure (don't share it)
- Use HTTPS in production
- Regularly backup your database
- Consider using environment variables for sensitive settings
- The encryption key is derived from Django's SECRET_KEY

## Troubleshooting

- If you get import errors, make sure all packages from requirements.txt are installed
- If templates aren't found, verify the TEMPLATES setting in settings.py
- For database issues, try deleting db.sqlite3 and running migrations again