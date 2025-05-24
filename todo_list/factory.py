from flask import Flask
from .api.todo import todolist


def create_app() -> Flask:
    app = Flask("todo_list")

    # config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

    app.register_blueprint(todolist)

    return app
