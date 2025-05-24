from typing import Optional


from todo_list.models.todo import ToDoItem, TodoStatus
from todo_list.models.base import db


class ToDoCRUDService:
    @staticmethod
    def create_todo(*, title: str, detail: Optional[str] = "") -> dict:
        todo = ToDoItem(title=title, detail=detail)  # type:ignore
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict()

    @staticmethod
    def get_todos() -> list[dict]:
        todos = (
            db.session.execute(db.select(ToDoItem).order_by(ToDoItem.created_at))
            .scalars()
            .all()
        )

        return [todo.to_dict() for todo in todos]

    @staticmethod
    def delete_todo(*, id: int) -> None:
        todo = db.get_or_404(ToDoItem, id)
        db.session.delete(todo)
        db.session.commit()

    @staticmethod
    def update_todo(*, id: int, title: str, detail: str, status: TodoStatus) -> dict:
        todo = db.get_or_404(ToDoItem, id)
        todo.title = title
        todo.detail = detail
        todo.status = status
        db.session.commit()

        return todo.to_dict()
