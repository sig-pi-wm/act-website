from flask_sqlalchemy import SQLAlchemy
from .definition import Base

class Client:
    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
        db = SQLAlchemy(model_class=Base)
        db.init_app(app)
