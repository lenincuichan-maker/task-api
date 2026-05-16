from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task Manager API",
    description="Mini API para gestionar tareas del curso de Metodologías de Desarrollo",
    version="1.0.0"
)

class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


tasks: list[Task] = []
next_id = 1


@app.get("/")
def home():
    return {
        "message": "Bienvenido a Task Manager API",
        "docs": "/docs"
    }


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks")
def create_task(task_data: TaskCreate):
    global next_id

    new_task = Task(
        id=next_id,
        title=task_data.title,
        description=task_data.description,
        completed=False
    )

    tasks.append(new_task)
    next_id += 1

    return {
        "message": "Tarea creada correctamente",
        "task": new_task
    }


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    for task in tasks:
        if task.id == task_id:
            task.completed = True

            return {
                "message": "Tarea marcada como completada",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )