#  Heroes & Powers API

A Flask REST API for managing heroes, their powers, and strength levels. The system allows assigning powers to heroes and notifies via email when a power is added.

---

## Features

- View all heroes and their super names
- View a single hero with their assigned powers
- List all available powers
- Update power descriptions (with validation)
- Assign powers to heroes with strength levels (e.g., Strong, Weak)
- Send email notifications when a power is assigned (using Flask-Mail)

---

## Technologies Used

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask-Mail
- SQLite (Development DB)
- Python Dotenv (`python-dotenv`)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/TheWilliams254/Superheroes.git
cd heroes-api
```
### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  
```
#### On Windows: 
```bash
venv\Scripts\activate
```
### 3. Install the Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
Create a .env file in the root folder and add your email credentials:

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```
 Use an App Password, not your Gmail login password!

### 5. Set Up the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
### 6. Seed the Database (Optional)
```bash
python seed.py
```
### API Endpoints
| Method | Route             | Description                           |
|--------|-------------------|---------------------------------------|
| GET    | `/heroes`         | Get all heroes                        |
| GET    | `/heroes/<id>`    | Get a hero and their powers           |
| GET    | `/powers`         | Get all powers                        |
| GET    | `/powers/<id>`    | Get a single power                    |
| PATCH  | `/powers/<id>`    | Update a power's description          |
| POST   | `/hero_powers`    | Assign a power to a hero (with email) |


### Sample POST /hero_powers Body
```json
{
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}
```
### Email Notifications
When a power is assigned to a hero, an email is automatically sent to the configured recipient with the hero’s name, power, and strength level.

### Project Structure
```bash
heroes-api/
├── instance
    ├── heroes.db
├── app.py
├── models.py
├── server
    ├── __init__.py
├venv
├── seed.py
├── .env
├── README.md
├── requirements.txt
└── migrations/
```
### Author
William Wambugu Ndiritu
williamwambugu663@gmail.com
0746662805

### License
This project is open source and available under the [MIT License](LICENSE).