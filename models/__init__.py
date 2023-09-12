"""This module contains the configuration settings of the app."""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hng_crud_project.db"
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


# pylint: disable=wrong-import-position
import models.register_model
