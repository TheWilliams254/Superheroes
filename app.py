from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

from models import db, Hero, Power, HeroPower

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuring mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

@app.route('/')
def index():
    return 'Superhero API is running!!'

@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:hero_id>')
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:power_id>')
def get_power(power_id):
    power = Power.query.get(power_id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description", "").strip()

    if not description or len(description) < 10:
        return jsonify({"errors": ["Description must be at least 10 characters."]}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict()), 200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    required_fields = ['hero_id', 'power_id', 'strength']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing one or more required fields"}), 400

    try:
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])

        if not hero or not power:
            return jsonify({"error": "Invalid hero_id or power_id"}), 400

        hero_power = HeroPower(
            hero_id=hero.id,
            power_id=power.id,
            strength=data['strength']
        )
        db.session.add(hero_power)
        db.session.commit()

        # Email
        msg = Message(
            subject=f"{hero.super_name} gained a new power!",
            recipients=["hawkswilliams000@gmail.com"],
            body=f"{hero.name} has been granted the power of {power.name} with strength: {hero_power.strength}."
        )
        mail.send(msg)

        return jsonify(hero_power.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)
