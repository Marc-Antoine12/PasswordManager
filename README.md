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