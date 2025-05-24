from flask import Blueprint


todolist = Blueprint("todolist", __name__, url_prefix="/todo")


@todolist.get("/")
def get_todos():
    return "hello"
