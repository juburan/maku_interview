from flask import Flask
from .api.todo import todolist
from .models.base import db


def create_app() -> Flask:
    app = Flask("todo_list")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

    app.register_blueprint(todolist)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
