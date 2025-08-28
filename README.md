🎓 Project Evaluation System


A Django-based Academic Project Evaluation System that makes grading fair, transparent, and rubric-driven.
Designed for coordinators, students, and panelists to collaborate seamlessly.

✨ Key Features

✅ Coordinator Dashboard – Create teams, add students, track phase-wise performance
✅ Student Dashboard – Upload GitHub repo & phase deliverables, check evaluations
✅ Panelist Dashboard – Conduct rubric-based evaluations with 15+ criteria
✅ Real-time Insights – Automatic average & total score calculations across phases
✅ Multi-phase Evaluation – Manage Phase 1, 2, and 3 submissions & scores

🖥️ Tech Stack
Layer	Technology
Backend	Django (Python 3.x)
Database	SQLite (default, can switch to PostgreSQL/MySQL)
Frontend	Django Templates + Bootstrap 5 + Custom CSS
Deployment	Localhost (dev) → Easily extendable for production
🚀 Getting Started
1️⃣ Clone the repo
git clone https://github.com/your-username/project-evaluation-system.git
cd project-evaluation-system

2️⃣ Create & activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Run the server
python manage.py runserver


➡️ Open: http://127.0.0.1:8000/

📊 Dashboards

👨‍🏫 Coordinator → /evaluation/coordinator/

🧑‍🎓 Student/Team → /evaluation/team/<team_id>/

🧑‍⚖️ Panelist → /evaluation/panelist/

📂 Project Structure
project-evaluation-system/
│── manage.py
│── project_eval_system/        # Project settings
│── evaluation/                 # Core app
│   ├── models.py               # Database models
│   ├── forms.py                # Forms for team & evaluations
│   ├── views.py                # Business logic
│   ├── urls.py                 # App routes
│   ├── templates/evaluation/   # HTML templates
│   └── migrations/             # Database schema migrations

⚙️ Configuration

Database → SQLite by default (edit settings.py to use PostgreSQL/MySQL)

Media files → Uploaded repos & phase files stored under /media/

Static files → Handled by Django static configuration

🤝 Contributing

Contributions make this project better 🎉

Fork the repo

Create your branch: git checkout -b feature-name

Commit: git commit -m "Add new feature"

Push: git push origin feature-name

Open a Pull Request

📸


<img width="472" height="229" alt="image" src="https://github.com/user-attachments/assets/370113c5-243b-40c2-b606-80a80d808d52" />
<img width="467" height="272" alt="image" src="https://github.com/user-attachments/assets/ec477869-0001-46c2-9c08-f75725bfac2d" />
<img width="470" height="266" alt="image" src="https://github.com/user-attachments/assets/766c2943-ac20-431f-a7b1-50513ff98dbb" />
<img width="466" height="251" alt="image" src="https://github.com/user-attachments/assets/e5ce79da-5c08-44b5-82fe-b6972c9bade5" />
<img width="475" height="261" alt="image" src="https://github.com/user-attachments/assets/3ca8a824-0503-420c-af27-67cdf45a36b4" />





📜 License

This project is licensed under the MIT License – you’re free to use, modify, and distribute with attribution.

🔥 With this system, evaluations are no longer tedious spreadsheets – everything is streamlined, rubric-driven, and transparent!
