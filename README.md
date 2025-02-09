# Hussain's Blog - Personal Blogging Platform


A personal blogging platform showcasing Hussain's journey from civil engineering to data science, featuring technical blog posts and professional insights.

## Features

- 🚀 **Home Page** with featured blog posts
- 📚 **Blog Details** with comments functionality
- 🔍 **Search functionality** across all blog posts
- 📄 **About Me** page with professional journey and resume
- 📧 **Contact Form** with success confirmation
- 💬 **Commenting System** for blog posts
- 🎨 **Responsive Design** using Bootstrap
- 🔒 **Admin Interface** for content management



# Blogging Django Project

This project is a simple blogging application built using the Django framework. It allows users to browse blog posts, read details, leave comments, contact the author, and search for specific content.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Models](#models)
- [Templates](#templates)
- [Forms](#forms)
- [URLs](#urls)
- [Views](#views)



## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/iamhussaink/blogs/.git]
## Installation
 **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blogging.git
   cd blogging

Project Structure
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


**# Technologies Used**

- Python
- Django
- HTML
- CSS
- Bootstrap

**# Models**

**## Blogs**
- title: CharField
- content: TextField
- created_date: DateTimeField
- image: ImageField

**## Comment**
- blog: ForeignKey(Blogs)
- email: EmailField
- comment: TextField
- created_date: DateTimeField

**## Contact_me**
- email: EmailField
- subject: TextField
- message: TextField
- timestamp: DateTimeField

**# Templates**

- **base.html**: Base template with common layout elements.
- **home.html**: Displays a list of blog posts.
- **blog_detail.html**: Displays the details of a single blog post and comments.
- **aboutme.html**: About me page content.
- **contact.html**: Contact form.
- **contact_success.html**: Confirmation page after successful contact form submission.
- **search.html**: Search results page.

**# Forms**

- **CommentForm**: Form for submitting comments.
- **ContactForm**: Form for contacting the author.

**# URLs**

- `/` → Home page
- `/home/` → Home page
- `/aboutme/` → About me page
- `/contact/` → Contact page
- `/search/` → Search results page
- `/blog/<int:pk>/` → Blog detail page
- `/contact/success/` → Contact success page

**# Views**

- **home**: Displays the home page with blog posts.
- **aboutme**: Displays the about me page.
- **contact**: Handles the contact form submission.
- **blog_detail**: Displays a single blog post and handles comments.
- **search**: Handles search queries and displays results.
- **contact_success**: Displays the contact success page.



