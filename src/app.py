"""Aplicação Flask do gerenciador de tarefas TechFlow."""

from __future__ import annotations

from flask import Flask, jsonify, redirect, render_template, request, url_for

from .models import TaskPriority, TaskStatus
from .storage import TaskStorage

storage = TaskStorage()

STATUS_LABELS = {
    TaskStatus.TODO.value: "A fazer",
    TaskStatus.IN_PROGRESS.value: "Em progresso",
    TaskStatus.DONE.value: "Concluído",
}

PRIORITY_LABELS = {
    TaskPriority.BAIXA.value: "Baixa",
    TaskPriority.MEDIA.value: "Média",
    TaskPriority.ALTA.value: "Alta",
}


def _wants_json() -> bool:
    if request.is_json:
        return True
    best = request.accept_mimetypes.best_match(["application/json", "text/html"])
    return (
        best == "application/json"
        and request.accept_mimetypes[best] > request.accept_mimetypes["text/html"]
    )


def _parse_status(raw: str | None):
    if raw is None:
        return None
    return TaskStatus(raw)


def _parse_priority(raw: str | None):
    if raw is None:
        return None
    return TaskPriority(raw)


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/")
    def index():
        """Board Kanban com modais de criação e detalhes."""
        tasks = storage.list_all()
        columns = [
            {
                "key": TaskStatus.TODO.value,
                "label": STATUS_LABELS[TaskStatus.TODO.value],
                "tasks": [t for t in tasks if t.status == TaskStatus.TODO],
            },
            {
                "key": TaskStatus.IN_PROGRESS.value,
                "label": STATUS_LABELS[TaskStatus.IN_PROGRESS.value],
                "tasks": [t for t in tasks if t.status == TaskStatus.IN_PROGRESS],
            },
            {
                "key": TaskStatus.DONE.value,
                "label": STATUS_LABELS[TaskStatus.DONE.value],
                "tasks": [t for t in tasks if t.status == TaskStatus.DONE],
            },
        ]
        return render_template(
            "index.html",
            columns=columns,
            all_tasks=tasks,
            labels=STATUS_LABELS,
            priority_labels=PRIORITY_LABELS,
        )

    @app.get("/tasks")
    def list_tasks():
        """Lista todas as tarefas cadastradas."""
        tasks = [task.to_dict() for task in storage.list_all()]
        return jsonify(tasks), 200

    @app.get("/tasks/<task_id>")
    def get_task(task_id: str):
        """Retorna uma tarefa pelo id."""
        task = storage.get(task_id)
        if task is None:
            return jsonify({"erro": "Tarefa não encontrada."}), 404
        return jsonify(task.to_dict()), 200

    @app.post("/tasks")
    def create_task():
        """Cria uma nova tarefa (JSON ou formulário)."""
        payload = request.get_json(silent=True) or {}
        title = payload.get("title") or request.form.get("title", "")
        description = payload.get("description") or request.form.get("description", "")
        status_raw = payload.get("status") or request.form.get(
            "status", TaskStatus.TODO.value
        )
        priority_raw = payload.get("priority") or request.form.get(
            "priority", TaskPriority.MEDIA.value
        )

        try:
            status = _parse_status(status_raw)
            priority = _parse_priority(priority_raw)
        except ValueError:
            if _wants_json():
                return jsonify({"erro": "Status ou prioridade inválidos."}), 400
            return redirect(url_for("index"))

        try:
            task = storage.create(
                title=title,
                description=description,
                status=status,
                priority=priority,
            )
        except ValueError as exc:
            if _wants_json():
                return jsonify({"erro": str(exc)}), 400
            return redirect(url_for("index"))

        if _wants_json():
            return jsonify(task.to_dict()), 201
        return redirect(url_for("index"))

    @app.put("/tasks/<task_id>")
    @app.post("/tasks/<task_id>/update")
    def update_task(task_id: str):
        """Atualiza título, descrição, status e/ou prioridade."""
        if storage.get(task_id) is None:
            if _wants_json() or request.method == "PUT":
                return jsonify({"erro": "Tarefa não encontrada."}), 404
            return redirect(url_for("index"))

        payload = request.get_json(silent=True) or {}
        title = payload.get("title") if "title" in payload else request.form.get("title")
        description = (
            payload.get("description")
            if "description" in payload
            else request.form.get("description")
        )
        status_raw = (
            payload.get("status") if "status" in payload else request.form.get("status")
        )
        priority_raw = (
            payload.get("priority")
            if "priority" in payload
            else request.form.get("priority")
        )

        try:
            status = _parse_status(status_raw)
            priority = _parse_priority(priority_raw)
        except ValueError:
            if _wants_json() or request.method == "PUT":
                return jsonify({"erro": "Status ou prioridade inválidos."}), 400
            return redirect(url_for("index"))

        try:
            updated = storage.update(
                task_id,
                title=title,
                description=description,
                status=status,
                priority=priority,
            )
        except ValueError as exc:
            if _wants_json() or request.method == "PUT":
                return jsonify({"erro": str(exc)}), 400
            return redirect(url_for("index"))

        if _wants_json() or request.method == "PUT":
            return jsonify(updated.to_dict()), 200
        return redirect(url_for("index"))

    @app.delete("/tasks/<task_id>")
    @app.post("/tasks/<task_id>/delete")
    def delete_task(task_id: str):
        """Remove uma tarefa pelo id."""
        deleted = storage.delete(task_id)
        if not deleted:
            if _wants_json() or request.method == "DELETE":
                return jsonify({"erro": "Tarefa não encontrada."}), 404
            return redirect(url_for("index"))
        if _wants_json() or request.method == "DELETE":
            return jsonify({"mensagem": "Tarefa removida com sucesso."}), 200
        return redirect(url_for("index"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
