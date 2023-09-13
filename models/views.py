"""This model defines class PersonResource."""
from flask_restful import Resource, reqparse
from models import db
from models.user import Person
from models.serializer import PersonSchema


class PersonResource(Resource):
    """This class defines methods to create, get, update, delete user."""

    user_schema = PersonSchema()
    users_schema = PersonSchema(many=True)

    def get(self, user_id=None):
        """
        This method returns a user if user_id is not None and is found in the database.
        It also returns an error message if user_id is not found in the database.
        However, it returns all users if user_id is None or empty list if no user is
        found in the database.
        """
        if user_id:
            user = Person.query.get(user_id)
            if user:
                user_data = self.user_schema.dump(user)
                return user_data

            return {'error': 'User not found.'}, 404

        users = Person.query.all()
        users_data = self.users_schema.dump(users)
        return users_data

    def post(self):
        """This method creates a new Person object and saves it in the database."""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Name is required.")
        args = parser.parse_args()

        name = args['name']

        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()

        person_data = self.user_schema.dump(new_person)

        return person_data, 201

    def put(self, user_id):
        """This method updates a person full information in the database."""
        if not user_id:
            return {'error': 'user_id is required.'}, 400

        person = Person.query.get(user_id)

        if not person:
            return {'error': 'User not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="Name is required.")
        args = parser.parse_args()

        person.name = args['name']
        db.session.commit()

        person_data = self.user_schema.dump(person)
        return person_data

    def patch(self, user_id):
        """Updates the some records of a person in the database."""
        if not user_id:
            return {'error': 'User id is required.'}, 400

        person = Person.query.get(user_id)

        if not person:
            return {'error': 'User not found.'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        if args['name'] is not None:
            person.name = args['name']
            db.session.commit()

        person_data = self.user_schema.dump(person)
        return person_data

    def delete(self, user_id):
        """This method deletes a person information from the database."""
        if not user_id:
            return {'error': 'User id is required.'}, 400

        person = Person.query.get(user_id)

        if not person:
            return {'error': 'User not found'}, 404

        db.session.delete(person)
        db.session.commit()

        return {'message': f'User {person.name} successfully deleted.'}
