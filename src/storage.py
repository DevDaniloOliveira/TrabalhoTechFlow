"""Persistência simples de tarefas em arquivo JSON."""

from __future__ import annotations

import json
from pathlib import Path

from .models import Task, TaskStatus

DEFAULT_DATA_PATH = Path(__file__).resolve().parent / "data" / "tasks.json"


class TaskStorage:
    """CRUD em memória com gravação em JSON."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or DEFAULT_DATA_PATH
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._tasks: dict[str, Task] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            self._tasks = {}
            return
        raw = json.loads(self.path.read_text(encoding="utf-8") or "[]")
        self._tasks = {item["id"]: Task.from_dict(item) for item in raw}

    def _save(self) -> None:
        payload = [task.to_dict() for task in self._tasks.values()]
        self.path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def create(self, title: str, description: str = "", status: TaskStatus | str = TaskStatus.TODO) -> Task:
        task = Task(title=title, description=description, status=status)
        self._tasks[task.id] = task
        self._save()
        return task

    def update(
        self,
        task_id: str,
        *,
        title: str | None = None,
        description: str | None = None,
        status: TaskStatus | str | None = None,
    ) -> Task | None:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description
        new_status = status if status is not None else task.status
        updated = Task(
            id=task.id,
            title=new_title,
            description=new_description,
            status=new_status,
        )
        self._tasks[task_id] = updated
        self._save()
        return updated

    def delete(self, task_id: str) -> bool:
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        self._save()
        return True
