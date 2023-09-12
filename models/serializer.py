"""This module defines class PersonSchema."""
from models import ma
from models.user import Person


class PersonSchema(ma.Schema):
    """
    This class automatically generates serialization and deserialization
    methods based on the Person model.
    """
    class Meta:
        """Defines the model"""
        model = Person
        fields = ('id', 'name')
