# Hussain's Blog - Personal Blogging Platform

A personal blogging platform showcasing Hussain's journey from civil engineering to data science, featuring technical blog posts, professional insights, and interactive discussions.

## Key Features

- 🚀 **Home Page** – Browse featured blog posts.
- 📚 **Blog Details** – Read blog posts with a commenting system.
- 🔍 **Search** – Find relevant blog posts easily.
- 📄 **About Me** – Learn about Hussain's professional journey and access his resume.
- 📧 **Contact Form** – Connect with Hussain via a simple form with success confirmation.
- 💬 **Commenting System** – Engage with content through comments.
- 🎨 **Responsive Design** – Built using Bootstrap for a seamless experience across devices.
- 🔒 **Admin Interface** – Manage blog content efficiently.

---

# Blogging Django Project

This project is a blogging application built with Django. It enables users to browse, read, comment on blog posts, contact the author, and search for specific content.

## Table of Contents

1. [Features](#key-features)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [Models](#models)
6. [Templates](#templates)
7. [Forms](#forms)
8. [URLs](#urls)
9. [Views](#views)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iamhussaink/blogs.git
   cd blogging
   ```  
2. **Set up a virtual environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```  
3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```  
4. **Run migrations:**  
   ```bash
   python manage.py migrate
   ```  
5. **Create a superuser for admin access:**  
   ```bash
   python manage.py createsuperuser
   ```  
6. **Start the development server:**  
   ```bash
   python manage.py runserver
   ```  

---

## Project Structure

```
blogging/
├── blog/
│   ├── templates/
│   │   └── blog/
│   │       ├── aboutme.html
│   │       ├── base.html
│   │       ├── blog_detail.html
│   │       ├── contact.html
│   │       ├── contact_success.html
│   │       ├── home.html
│   │       └── search.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogging/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
```

---

## Technologies Used

- **Python**
- **Django**
- **HTML & CSS**
- **Bootstrap**

---

## Models

### **Blog**
- `title`: CharField
- `content`: TextField
- `created_date`: DateTimeField
- `image`: ImageField

### **Comment**
- `blog`: ForeignKey(Blogs)
- `email`: EmailField
- `comment`: TextField
- `created_date`: DateTimeField

### **ContactMe**
- `email`: EmailField
- `subject`: TextField
- `message`: TextField
- `timestamp`: DateTimeField

---

## Templates

- **base.html** – Common layout template.
- **home.html** – Displays a list of blog posts.
- **blog_detail.html** – Blog post details and comments.
- **aboutme.html** – About me page.
- **contact.html** – Contact form.
- **contact_success.html** – Contact form submission success page.
- **search.html** – Search results page.

---

## Forms

- **CommentForm** – Form for submitting comments.
- **ContactForm** – Form for contacting the author.

---

## URLs

- `/` → Home page
- `/aboutme/` → About me page
- `/contact/` → Contact page
- `/search/` → Search results page
- `/blog/<int:pk>/` → Blog detail page
- `/contact/success/` → Contact success page

---

## Views

- **home** – Displays the home page with blog posts.
- **aboutme** – Displays the about me page.
- **contact** – Handles the contact form submission.
- **blog_detail** – Displays a single blog post and handles comments.
- **search** – Handles search queries and displays results.
- **contact_success** – Displays the contact success page.

---

## License

This project is open-source and available under the MIT License.

---

## Author

👨‍💻 **Hussain** – Follow my journey from civil engineering to data science through my blogs!


🌎 GitHub: [github.com/yourusername](https://github.com/iamhussaink

