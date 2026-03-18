# 💻 Django Projects

A collection of web applications built with Python and Django.

---

## 📂 Projects

### 1. 📝 Blog App
A full-featured blogging platform where users can write, publish, and discuss posts.

### 2. ✅ Todo App
A task management app to create, track, and complete daily tasks.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite3
- **Tools:** VS Code, Git, GitHub

---

## ⚙️ Setup & Installation

These steps work for both projects.

### 1. Clone the repository
```bash
git clone https://github.com/DSBaibhav/yourrepo.git
cd yourrepo
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create an admin account
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000
```

---

## 📝 Blog App — Features

- User login and logout
- Create, edit, and delete blog posts
- Upload cover images for posts
- Comment on posts
- Delete your own comments
- Pagination on home page
- Clean responsive UI

---

## ✅ Todo App — Features

- Add and delete tasks
- Mark tasks as complete or incomplete
- Simple and minimal interface
- User-specific task lists

---

## 📁 Project Structure
```
repo/
├── app1/                   # Blog application
│   ├── templates
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── blog/                   # Todo application
│   ├── templates/blog/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 🔑 Admin Panel
```
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials to manage all data.

---

## 🙋‍♂️ Author

**Baibhav Singh**
Built with Django on macOS using VS Code.

---

## 📄 License

These projects are for personal and educational use.
