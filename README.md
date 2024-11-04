# Time Table Management System

A Django web application for managing and organizing academic timetables. This system allows administrators to create, update, and view schedules for different classes, faculties, and rooms.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Admin Dashboard**: Manage courses, faculties, rooms, and students.
- **Time Table Generation**: Create schedules with automatic conflict detection.
- **Role-Based Access Control**: Separate dashboards for administrators, faculty, and students.
- **Responsive Design**: Accessible on both desktop and mobile.

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+
- Virtual Environment Tool (e.g., `venv`)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/timetable-management-system.git
    cd timetable-management-system
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000`.

## Project Structure

![s1](https://github.com/user-attachments/assets/711817fd-45ce-4d21-b6ad-0cc801b33a1b)
![s2](https://github.com/user-attachments/assets/eb30aa9d-31e4-4d68-9814-2a18d6f826da)
![s3](https://github.com/user-attachments/assets/641862bd-01ab-4a46-adf8-758bdfc14a3e)
![s4](https://github.com/user-attachments/assets/af4a6f4a-f8df-4f3d-b565-fbf34a061863)
![s5](https://github.com/user-attachments/assets/6c14e962-0235-4752-860f-ac78359318f7)
![s7](https://github.com/user-attachments/assets/d10b81ce-53e2-4eef-a8aa-f42326f74918)
![s8](https://github.com/user-attachments/assets/965ee51b-59b0-4aad-9e01-2cbf94f463fa)
![s9](https://github.com/user-attachments/assets/5557907d-528d-475f-8ba2-6676ab11e025)
![s10](https://github.com/user-attachments/assets/7fc097dd-5c1f-4fc5-bec6-dfb04e1e2e31)
![s11](https://github.com/user-attachments/assets/fb4fd202-2330-48a1-a89c-65a170d433b8)

```plaintext
timetable-management-system/
├── attendance/                # App for managing attendance
├── courses/                   # App for managing course details
├── exam_timetable/            # App for scheduling exams
├── schedule/                  # Core scheduling logic
├── users/                     # User management (registration, roles)
├── templates/                 # HTML templates
├── static/                    # Static files (CSS, JS, images)
├── db.sqlite3                 # SQLite Database (default)
├── manage.py                  # Django's command-line utility
└── README.md                  # Project documentation



