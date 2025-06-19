# Heroes & Powers API

A Flask-based RESTful API for managing heroes, their superpowers, and strength levels. Includes email notifications when powers are assigned using **Flask-Mail**.

---

## Features

- View all heroes and their super names
- View individual heroes with their powers
- List all powers
- Update power descriptions with validation
- Assign powers to heroes (with strength level)
- Sends email notifications when a new power is assigned

---

## Technologies

- Python & Flask
- SQLAlchemy ORM
- SQLite (development)
- Flask-Migrate (Alembic)
- Flask-Mail (SMTP email support)
- python-dotenv

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TheWilliams254/heroes-api.git
cd heroes-api

---
 ### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

---
