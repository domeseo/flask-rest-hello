from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship, declarative_base
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from eralchemy2 import render_er

db = SQLAlchemy()


class User(db.Model):

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(40), nullable=False)

    favorites = relationship('Favorite', backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):

    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=True)
    climate = Column(String(100), nullable=False)
    gravity = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)

    favorites = relationship('Favorite', backref="planet")


class Characters(db.Model):

    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(10), nullable=False)
    eyes_color = Column(String(10), nullable=False)
    race = Column(String(20), nullable=False)
    planet_origin = Column(String(50), nullable=False)

    favorite = relationship('Favorite', backref="characters")


class Vehicles(db.Model):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False)
    pilot = Column(String(100), nullable=True)
    speed = Column(Integer, nullable=False)
    color = Column(String(10), nullable=False)
    lenght = Column(Integer, nullable=False)
    vehicle_class = Column(String(100), nullable=False)

    favorites = relationship('Favorite', backref="vehicles")


class Favorite(db.Model):

    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))


render_er(db.Model, 'diagram.png')
