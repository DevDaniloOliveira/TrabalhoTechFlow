"""Modelo de domínio Task (inclui prioridade após mudança de escopo)."""

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


class TaskPriority(str, Enum):
    """Prioridade da tarefa (mudança de escopo — logística)."""

    BAIXA = "baixa"
    MEDIA = "media"
    ALTA = "alta"

    @classmethod
    def values(cls) -> set[str]:
        return {p.value for p in cls}

    @property
    def rank(self) -> int:
        """Maior número = mais urgente (para ordenação)."""
        return {self.BAIXA: 1, self.MEDIA: 2, self.ALTA: 3}[self]


@dataclass
class Task:
    """Representa uma tarefa do gerenciador TechFlow."""

    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIA
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        if isinstance(self.status, str):
            self.status = TaskStatus(self.status)
        if isinstance(self.priority, str):
            self.priority = TaskPriority(self.priority)
        title = (self.title or "").strip()
        if not title:
            raise ValueError("O título da tarefa é obrigatório.")
        self.title = title
        self.description = (self.description or "").strip()

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["priority"] = self.priority.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Task:
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            status=TaskStatus(data.get("status", TaskStatus.TODO.value)),
            priority=TaskPriority(data.get("priority", TaskPriority.MEDIA.value)),
        )
