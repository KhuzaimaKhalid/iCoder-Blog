````markdown
# iCoder Blog

A simple Django-based blog application with rich‐text editing powered by **Django CKEditor 5**.

---

## 🎬 Tutorial

This project was built by following the “Harry” Django blog playlist on YouTube (starting from **video 72**)—but swapping out TinyMCE for the more powerful [Django CKEditor 5](https://github.com/django-ckeditor/django-ckeditor-5).

You can watch the full playlist here:  
https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9

---

## 🚀 Features

- User registration, login & logout  
- Create, edit & delete blog posts  
- Rich‐text editor (CKEditor 5) for post body  
- Post categories & thumbnails  
- “Continue reading” teaser on home page  
- Popular posts widget (by view count)  
- Commenting on posts  
- Contact form with validation & email notifications  
- Responsive Bootstrap 5 UI  

---

## 🛠️ Built With

- [Python 3.x](https://www.python.org/)  
- [Django 5.x](https://www.djangoproject.com/)  
- [Django CKEditor 5](https://github.com/django-ckeditor/django-ckeditor-5)  
- [Bootstrap 5](https://getbootstrap.com/)  
- SQLite (default; changeable in `settings.py`)  

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/KhuzaimaKhalid/iCoder-Blog.git
   cd iCoder-Blog
````

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Linux/macOS
   .venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

6. **Create a superuser (for admin)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🗂️ Project Structure

```
iCoder-Blog/
├── blog/                # Blog app (models, views, templates)
├── home/                # Home & contact app
├── static/              # CSS, JS, images
├── templates/           # Base templates & includes
├── media/               # Uploaded thumbnails
├── iCoder/              # Project settings
├── db.sqlite3           # SQLite database
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add foo feature'`)
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request


