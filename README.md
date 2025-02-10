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
![Screenshot (236)](https://github.com/user-attachments/assets/1dbf34d8-8ab2-455b-a4ce-d2be23c276e8)

![Screenshot (237)](https://github.com/user-attachments/assets/6fcf2003-ce69-4221-ac16-67c75ba988d0)

![Screenshot (238)](https://github.com/user-attachments/assets/f5577c5b-15a4-4474-8e55-19993826eb2d)

![Screenshot (239)](https://github.com/user-attachments/assets/5d69bfc5-f248-4020-9842-92d3f306b241)



![Screenshot (240)](https://github.com/user-attachments/assets/2413fe44-b8ad-4191-a2a0-8b46ad13b0e0)


![Screenshot (241)](https://github.com/user-attachments/assets/65622e94-6e69-4db7-a0a9-f9bb8b7b7261)


![Screenshot (242)](https://github.com/user-attachments/assets/8be89540-0f88-4a33-a507-bb31c4987dec)


![Screenshot (243)](https://github.com/user-attachments/assets/3cae9385-4d67-4245-9d8b-247cd629af00)


![Screenshot (242) - Copy](https://github.com/user-attachments/assets/fe3dd6a7-5720-41d2-85ac-2d30c5903273)


![Screenshot (245)](https://github.com/user-attachments/assets/7f0520e1-c14b-44e4-a934-92f7f7517c33)


![Screenshot (246)](https://github.com/user-attachments/assets/ed6fbc7a-5c96-41b0-963e-adabdc2e4e00)



## License

This project is open-source and available under the MIT License.

---

## Author

👨‍💻 **Hussain** – Follow my journey from civil engineering to data science through my blogs!


🌎 GitHub: [github.com/yourusername](https://github.com/iamhussaink

