from flask_sqlalchemy import SQLAlchemy
from .definition import Base, User
from .config import user, password, host, database

class Client:
    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{password}@{host}:5432/{database}"
        self.__db = SQLAlchemy(model_class=Base)
        self.__db.init_app(app)
        self.app = app

        with app.app_context():
            Base.metadata.create_all(bind=self.__db.engine)

    def test(self):
        with self.app.app_context():
            new_user = User(username="Matthew")
            self.__db.session.add(new_user)
            self.__db.session.commit()
            print(f"Inserted user with ID: {new_user.user_id}")

            # Query all users to verify
            users = self.__db.session.query(User).all()
            print("Current users in the database:")
            for user in users:
                print(f"User ID: {user.user_id}, Username: {user.username}")


