from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import backref, validates

from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    super_name = db.Column(db.String(80))

    hero_powers = db.relationship('HeroPower',back_populates='hero', cascade='all, delete-orphan')

    serialize_rules = ('-hero_powers.hero',)


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))

    hero_powers = db.relationship('HeroPower',back_populates='power',cascade='all, delete-orphan')

    serialize_rules = ('-hero_powers.power',)

    @validates('description')
    def validate_description(self , key ,description ):
        if not description or len(description.strip()) < 20:
            raise ValueError('The description must be at least 20 characters long')
        return description


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
   

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    @validates('strength')
    def validate_strength(self , key , strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("The strength must be either Strong, Weak or Average")
        return strength
    


    def __repr__(self):
        return f'<HeroPower {self.id} {self.hero_id} {self.power_id} {self.strength}>'