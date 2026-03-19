# ⬡ WorksNest

A modern full-stack job portal built with Django. WorksNest connects job seekers with recruiters through a clean, responsive interface with role-based dashboards, real-time application tracking, and a seamless hiring workflow.

---

## 🚀 Features

### Job Seekers
- Browse and search job listings by title, type, and location
- Apply to jobs with a cover letter and resume
- Track application status in real time (Applied → Reviewing → Shortlisted → Hired)
- Save jobs for later
- Personal profile with skills, bio, resume and social links

### Recruiters
- Post, edit, and manage job listings
- Company profile with logo and description
- View all applications per job listing
- Update applicant status with one click
- Dashboard with stats on active jobs and total applications

### General
- Role-based registration (Job Seeker / Recruiter)
- Secure login and logout
- Responsive design — works on mobile and desktop
- Dark navy UI with teal accents and 3D card animations
- Flash notifications for all actions

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Database | SQLite (dev) / PostgreSQL (production) |
| Frontend | HTML, CSS, Vanilla JS |
| Auth | Django built-in auth |
| Deployment | Render.com + Gunicorn + Whitenoise |
| Storage | Pillow for image handling |

---

## 📁 Project Structure

```
xproject/
├── WorksNest/          # Project config (settings, urls, wsgi)
├── core/               # Main app
│   ├── templates/
│   │   ├── core/       # All page templates
│   │   └── registration/
│   ├── templatetags/   # Custom template filters
│   ├── models.py       # Profile, Company, Job, Application, SavedJob
│   ├── views.py        # All views
│   ├── urls.py         # URL routing
│   ├── forms.py        # Django forms
│   └── admin.py        # Admin config
├── static/             # CSS and JS
├── media/              # User uploads
├── requirements.txt
├── Procfile
└── manage.py
```

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/xproject.git
cd xproject
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## 🌐 Deployment (Render.com)

### Environment Variables on Render
```
SECRET_KEY     →  your-generated-secret-key
DEBUG          →  False
ALLOWED_HOSTS  →  yourappname.onrender.com
DATABASE_URL   →  postgresql://... (from Render PostgreSQL)
```

### Build Command
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### Start Command
```
gunicorn WorksNest.wsgi
```

---

## 📸 Pages

| Page | URL |
|---|---|
| Home | `/` |
| Browse Jobs | `/jobs/` |
| Job Detail | `/jobs/<id>/` |
| Register | `/register/` |
| Login | `/login/` |
| Dashboard | `/dashboard/` |
| Profile | `/profile/` |
| Post a Job | `/recruiter/jobs/new/` |
| Company Profile | `/recruiter/company/` |
| My Applications | `/seeker/applications/` |
| Saved Jobs | `/seeker/saved/` |
| Admin Panel | `/admin/` |

---

## 👤 User Roles

**Job Seeker**
- Can browse, apply, save jobs
- Has personal profile with resume

**Recruiter**
- Can post and manage jobs
- Has company profile
- Can review and update application statuses

---

## 📄 License

©️ 2026 WorksNest. All rights reserved.
# WorksNest
# WorksNest
