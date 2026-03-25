# ⬡ WorksNest

A modern full-stack job portal web application built with Django, connecting job seekers with recruiters through a clean, responsive interface with role-based dashboards and real-time application tracking.

🌐 **Live Demo:** [https://worksnest.onrender.com](https://worksnest.onrender.com)

---

## 🚀 Features

### Job Seekers
- Browse and search job listings by title, type, and location
- Apply to jobs with a cover letter and resume
- Track application status in real time — Applied → Reviewing → Shortlisted → Hired / Rejected
- Save jobs for later
- Personal profile with skills, bio, resume and social links

### Recruiters
- Post, edit, and manage job listings
- Company profile with logo and description
- View all applications per job listing
- Update applicant status with one click
- Dashboard with stats on active jobs and total applications

### General
- Role-based registration — Job Seeker or Recruiter
- Secure login and logout
- Responsive design — works on mobile and desktop
- Dark navy UI with teal accents and smooth animations
- Flash notifications for all actions

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Language | Python 3.14 |
| Database | SQLite (dev) / PostgreSQL (production) |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Auth | Django built-in authentication |
| Server | Gunicorn (WSGI) |
| Static Files | Whitenoise |
| Deployment | Render.com |

---

## 📁 Project Structure

```
xproject/
├── WorksNest/              # Project config (settings, urls, wsgi)
├── core/                   # Main app
│   ├── templates/
│   │   ├── core/           # All page templates
│   │   └── registration/   # Login and register templates
│   ├── templatetags/       # Custom template filters
│   ├── models.py           # Profile, Company, Job, Application, SavedJob
│   ├── views.py            # All views
│   ├── urls.py             # URL routing
│   ├── forms.py            # Django forms
│   └── admin.py            # Admin configuration
├── static/                 # CSS and JS
├── media/                  # User uploads
├── requirements.txt
├── Procfile
├── runtime.txt
└── manage.py
```

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/DSBaibhav/WorksNest.git
cd WorksNest
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
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

## 🌐 Deployment

This project is deployed on **Render.com** using:
- **Gunicorn** as the production WSGI server
- **Whitenoise** for serving static files
- **PostgreSQL** as the production database

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
- Can browse, search, apply and save jobs
- Has personal profile with resume upload
- Can track application status in real time

**Recruiter**
- Can post and manage job listings
- Has company profile with logo
- Can review applications and update their status

---

## 👨‍💻 Author

**DSBaibhav**
- GitHub: [@DSBaibhav](https://github.com/DSBaibhav)

---

## 📄 License

©️ 2026 WorksNest. All rights reserved.
