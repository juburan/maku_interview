import enum
from typing import Any, Optional
from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .base import db


class TodoStatus(str, enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    HOLD = "hold"


class ToDoItem(db.Model):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    detail: Mapped[Optional[str]] = mapped_column(String(200))
    status: Mapped[TodoStatus] = mapped_column(Enum(TodoStatus), default=TodoStatus.NEW)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "detail": self.detail,
            "status": self.status,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
