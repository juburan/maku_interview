import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from .base import db


class TodoStatus(str, enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    DELETED = "deleted"
    HOLD = "hold"


class ToDoItem(db.Model):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    detail: Mapped[str]
    status: Mapped[TodoStatus] = mapped_column(Enum(TodoStatus), default=TodoStatus.NEW)
