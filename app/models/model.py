"""
This module defines the database models for the Flask API project.
It includes two primary models: "Owner", and "Pet". These models
represent the database tables and their relationships.

Classes:
    Owner:
        Represents an owner with attributes such as name, address, city and telephone.
        An owner can have multiple pets.
    
    Pet:
        Represents a pet with attributes such as name, birth_date, type and a foreign
        key to its owner. Each pet belongs to a single owner.

Relationships:
    One-to-Many: An "Owner" can have multiple "Pet" instances, but each "Pet"
    instance can only belong to one "Owner".
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    """
    Represents an owner with attributes such as name, address, city and telephone.
    An owner can have multiple pets.

    Attributes:
    ---------------
    id: int
        The unique identifier for the owner.
    name: string
        Name of the owner.
    address: string
        Address of the owner.
    city: string
        City of the owner.
    telephone: string
        Telephone of the owner.
    pets: list
        List of pets belonging to the owner.
    """
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    telephone = db.Column(db.String(25), nullable=False)

    pets = db.relationship('Pet', backref='owner', lazy=True)


    def serialize(self):
        """
        This function return owner's detail in a JSON format.
        """
        return {
            'id': self.id,
            'name':self.name,
            'address':self.address,
            'city':self.city,
            'telephone':self.telephone,
            'pets': [pet.serialize() for pet in self.pets]
        }

    @property
    def last_name(self):
        """
        This function split the owner's name and retrive it's last name for searching purpose. 
        """
        return self.name.split()[-1] if self.name else ''

class Pet(db.Model):
    """
    Represents a pet with attributes such as name, birth_date, type and a foreign
    key to its owner. Each pet belongs to a single owner.

    Attributes:
    ---------------
    id: int
        The unique identifier for the pet.
    name: string
        Name of the pet.
    birth_date: date
        Birth date of the pet.
    type: string
        Type of the owner.
    owner_id: int
        Foreign key referencing the owner of the pet.
    """
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date)
    type = db.Column(db.String(25))
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)

    def serialize(self):
        """
        This function return's pet's detail in a JSON format.
        """
        return {
            'id':self.id,
            'name':self.name,
            'birth_date':self.birth_date,
            'type':self.type
        }
