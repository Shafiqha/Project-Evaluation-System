# Project-Evaluation-System
Project Evaluation System
📌 Introduction

The Project Evaluation System is a Django-based web application designed to streamline academic project assessments using customizable rubrics. It allows coordinators, panelists, and students to interact within a centralized platform for transparent and structured evaluation across multiple phases.

The system supports:

Creating teams and assigning students.

Uploading project files (per phase).

Panelist evaluations using rubrics with scoring.

Real-time calculation of averages across phases.

Dashboards tailored for coordinators, panelists, and students.

📑 Table of Contents

Features

Tech Stack

Installation

Usage

System Roles

Project Structure

Configuration

Contributing

License

✨ Features

Coordinator Dashboard

Add students and create teams.

Track phase-wise and total average marks.

Student (Team) Dashboard

Upload project files for each phase.

View evaluations and averages.

Panelist Dashboard

Evaluate teams using detailed rubric criteria.

Input scores for multiple performance aspects.

Automatic calculation of total and average marks.

Rubric-based Evaluation
Covers aspects like:

Abstract & synopsis

Topic relevance

Problem identification

Methodology & literature survey

Documentation

Presentation & communication

Technical knowledge & involvement

Question handling & attitude

🛠 Tech Stack

Backend: Django 5.1.3, SQLite

Frontend: Django templates, Bootstrap 5, custom CSS

Language: Python 3.x

Deployment: Localhost (development), extendable for production

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/project-evaluation-system.git
cd project-evaluation-system


Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Run the development server

python manage.py runserver

🚀 Usage

Open the application at http://127.0.0.1:8000/

Navigate via dashboards:

Coordinator: /evaluation/coordinator/

Student: /evaluation/team/<team_id>/

Panelist: /evaluation/panelist/

👥 System Roles

Coordinator: Manages students, teams, and monitors evaluations.

Student (Team): Uploads project documents and checks scores.

Panelist: Conducts rubric-based evaluations per phase.

📂 Project Structure
project-evaluation-system/
│── manage.py
│── project_eval_system/        # Django project settings
│── evaluation/                 # Core app
│   ├── models.py               # Database models (Student, Team, Evaluation)
│   ├── forms.py                # Team & evaluation forms
│   ├── views.py                # Views for dashboards
│   ├── urls.py                 # App routes
│   ├── templates/evaluation/   # HTML templates
│   └── migrations/             # Database migrations

🔧 Configuration

Database: SQLite (default). Can be switched to PostgreSQL/MySQL in settings.py.

Media Files: Uploaded project files stored under /media/.

Static Files: Handled via Django static configuration.

🤝 Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch (git checkout -b feature-name).

Commit changes (git commit -m "Add feature").

Push to your fork and open a Pull Request.

📜 License

This project is licensed under the MIT License – feel free to use and adapt it for academic or research purposes.
