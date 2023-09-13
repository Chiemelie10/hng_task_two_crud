"""This module defines class TestApi."""
import unittest
import requests
from models.user import Person
from models import db, app
from models.serializer import PersonSchema

class TestApi(unittest.TestCase):
    """
    This class defines the attributes and methods for
    testing the API endpoints of the application.
    """

    url = "http://localhost:5000/api"

    data = {
        "name": "Test Name"
    }

    update = {
        "name": "Full Update"
    }

    partial_update = {
        "name": "Partial Update"
    }

    with app.app_context():
        id = 1
        new_user = Person(name="New User", id=id)
        db.session.add(new_user)
        db.session.commit()
        user = db.session.execute(db.select(Person).filter_by(id=id)).scalar()
        schema = PersonSchema()
        user_data = schema.dump(user)
        new_user_id = user_data['id']

    def test_1_get_users(self):
        """This method tests get all users."""
        response = requests.get(self.url, timeout=10)
        self.assertEqual(response.status_code, 200)
        print("Test 1 completed")

    def test_2_get_user(self):
        """This method tests get a user by ID."""
        response = requests.get(self.url + '/' + self.new_user_id, timeout=10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        print("Test 2 completed")

    def test_3_create_user(self):
        """This method tests create a user."""
        response = requests.post(self.url, json=self.data, timeout=10)
        self.assertEqual(response.status_code, 201)

        with app.app_context():
            #user = db.session.execute()
            user = db.session.execute(db.select(Person).
                                      filter_by(id=response.json()['id'])).scalar()
            db.session.delete(user)
            db.session.commit()

        print("Test 3 completed")

    def test_4_update_user(self):
        """This method tests update a user."""
        response = requests.put(self.url + '/' + self.new_user_id,
                                json=self.update, timeout=10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.update['name'])
        print("Test 4 completed")

    def test_5_partial_update_user(self):
        """This method tests update a user."""
        response = requests.patch(self.url + '/' + self.new_user_id,
                                  json=self.partial_update, timeout=10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.partial_update['name'])
        print("Test 5 completed")

    def test_6_delete_user(self):
        """This method tests update a user."""
        response = requests.delete(self.url + '/' + self.new_user_id, timeout=10)
        self.assertEqual(response.status_code, 200)
        print("Test 6 completed")


if __name__ == '__main__':
    tester = TestApi()
    tester.test_1_get_users()
    tester.test_2_get_user()
    tester.test_3_create_user()
    tester.test_4_update_user()
    tester.test_5_partial_update_user()
    tester.test_6_delete_user()
