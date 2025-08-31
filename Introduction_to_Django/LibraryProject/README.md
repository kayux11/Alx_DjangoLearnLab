# Introduction to Django Development Environment Setup

## 🎯 Objective

Gain familiarity with Django by setting up a development environment and creating a basic Django project.
This task introduces the workflow of Django projects, including project creation and running the development server.

---

## 📝 Task Description

You will:

* Install Django
* Create a new Django project named **LibraryProject**
* Run the development server
* Explore the project’s default structure to understand the roles of various components

This setup will serve as the foundation for developing Django applications.

---

## 🚀 Steps

### 1. Install Django

* Ensure Python is installed on your system.
* Install Django using pip:

  ```bash
  pip install django
  ```

---

### 2. Create Your Django Project

* Create a new Django project named **LibraryProject**:

  ```bash
  django-admin startproject LibraryProject
  ```

---

### 3. Run the Development Server

* Navigate into your project directory:

  ```bash
  cd LibraryProject
  ```

* Create a **README.md** file inside the `LibraryProject` folder.
* Start the development server:

  ```bash
  python manage.py runserver
  ```

* Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the default Django welcome page.

---

### 4. Explore the Project Structure

Familiarize yourself with the created project structure. Pay particular attention to:

* **`settings.py`** – Configuration for the Django project
* **`urls.py`** – The URL declarations for the project; acts like a “table of contents” for your Django-powered site
* **`manage.py`** – A command-line utility that lets you interact with this Django project

---

✅ You’re now ready to start building Django applications inside **LibraryProject**.
