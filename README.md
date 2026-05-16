# Task Manager API

Mini API para gestionar tareas, desarrollada como proyecto base del curso de Metodologías de Desarrollo.

## Objetivo del proyecto

Construir una aplicación pequeña que permita practicar flujo de trabajo moderno con Python, Git y GitHub.

## Funcionalidades iniciales

- Listar tareas.
- Crear tareas.
- Marcar tareas como completadas.

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Git
- GitHub

## Estructura del proyecto

```text
task-api/
├── app/
│   └── main.py
├── docs/
├── tests/
├── README.md
└── requirements.txt
```

## Ejecución local

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

```bash
venv\Scripts\Activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API

```bash
uvicorn app.main:app --reload
```

### 5. Abrir documentación

```text
http://127.0.0.1:8000/docs
```

## Estado del proyecto

Versión inicial del proyecto.

## Equipo de trabajo

Integrantes:

- Lenin Cuichan
- Juan Pablo Andagoya

## Convención de commits

El equipo utilizará mensajes de commit con el siguiente formato:

- feat: nueva funcionalidad
- fix: corrección de errores
- docs: cambios en documentación
- refactor: mejora interna del código
- test: pruebas
- chore: tareas de configuración