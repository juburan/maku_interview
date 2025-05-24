from flask import Blueprint, request, render_template

from todo_list.services.todo_crud import ToDoCRUDService


todolist = Blueprint("todolist", __name__, url_prefix="/todo")


@todolist.get("/")
def get_todos() -> list[dict]:
    return ToDoCRUDService.get_todos()


@todolist.post("/")
def create_todo() -> dict:
    title = request.form["title"]
    detail = request.form["detail"]
    return ToDoCRUDService.create_todo(title=title, detail=detail)


@todolist.delete("/<id>")
def delete_todo(id: int):
    ToDoCRUDService.delete_todo(id=id)
    return {}


@todolist.patch("/<id>")
def update_status(id: int) -> dict:
    title = request.form["title"]
    detail = request.form["detail"]
    status = request.form["status"]

    return ToDoCRUDService.update_todo(
        id=id,
        title=title,
        detail=detail,
        status=status,  # type: ignore
    )


@todolist.get("/html")
def render_todo_page():
    todos = ToDoCRUDService.get_todos()
    return render_template("todo.html", todos=todos)
