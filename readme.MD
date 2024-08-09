# Helpdesk Ticketing System

## Overview

This project is a Helpdesk Ticketing System built with Django. It is designed to manage helpdesk tickets and allow users to track and resolve issues efficiently. The system supports two user roles: Admin and Regular users, with different permissions for each role.

## Features

- User authentication (Sign up, Login, Forgot Password)
- Role-based access control (Admin and Regular users)
- CRUD operations for tickets
- Validation and error handling
- User-friendly interface with notifications

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.8 or higher)
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Run the following commands

- cd helpdesk
- python3 -m venv venv
- source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


By default, the server will start at http://127.0.0.1:8000/.
