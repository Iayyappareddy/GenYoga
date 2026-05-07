# GenYoga

GenYoga is an AI-powered yoga recommendation web application designed to help users find suitable yoga poses based on pain descriptions and duration.

---

## Features

- User Authentication
- AI-based Yoga Recommendation
- 30-Day Yoga Course
- Dynamic Pose Viewer
- Interactive Dashboard
- PostgreSQL Database Integration
- Responsive UI Design

---

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- CSS
- JavaScript
- Machine Learning
- Scikit-learn

---

## Project Structure

```bash
accounts/
dashboard/
recommendations/
templates/
static/
media/
ml_model/
manage.py
requirements.txt
README.md
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

### 2. Move Into Project Folder

```bash
cd GENYOGA
```

---

### 3. Create Virtual Environment

```bash
python -m venv env
```

---

### 4. Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Mac/Linux

```bash
source env/bin/activate
```

---

### 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

### 1. Install PostgreSQL

Download and install PostgreSQL and pgAdmin.

---

### 2. Create Database

Create database named:

```bash
genyoga
```

---

### 3. Update DATABASES in settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'genyoga',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Django Commands

### Make Migrations

```bash
python manage.py makemigrations
```

---

### Apply Migrations

```bash
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

---

### Run Development Server

```bash
python manage.py runserver
```

---

### Open Application

```bash
http://127.0.0.1:8000/
```

---

### Open Admin Panel

```bash
http://127.0.0.1:8000/admin/
```

---

## Machine Learning Integration

The application uses a Machine Learning model to:

- Predict pain category
- Predict severity level
- Recommend yoga poses dynamically

---


---

## Author

Ayyappa