from flask_sqlalchemy import SQLAlchemy
from .definition import Base, User
from .config import *

class Client:
    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}:5432/{database}"
        self.__db = SQLAlchemy(model_class=Base)
        self.__db.init_app(app)
        with app.app_context():
            self.__db.create_all()

    def test(self):
        result = self.__db.session.execute(self.__db.insert(User).values(username="Matthew"))
        rows = result.all()
        print(rows)
