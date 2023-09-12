"""This module defines the Person class."""
from uuid import uuid4
from models import db


class Person(db.Model):
    """This class defines the fields of the Person model"""
    __tablename__ = 'persons'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(100), nullable=False)

    def __str__(self):
        """Returns string representation of an instance of the class"""
        return f'{self.name}'
