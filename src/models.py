"""Modelo de domínio Task (escopo inicial, sem prioridade)."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class TaskStatus(str, Enum):
    """Status possíveis de uma tarefa no fluxo Kanban."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    @classmethod
    def values(cls) -> set[str]:
        return {s.value for s in cls}


@dataclass
class Task:
    """Representa uma tarefa do gerenciador TechFlow."""

    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.TODO
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        if isinstance(self.status, str):
            self.status = TaskStatus(self.status)
        title = (self.title or "").strip()
        if not title:
            raise ValueError("O título da tarefa é obrigatório.")
        self.title = title
        self.description = (self.description or "").strip()

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Task:
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            status=TaskStatus(data.get("status", TaskStatus.TODO.value)),
        )
