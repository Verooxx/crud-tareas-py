# CRUD de Tareas (Flask)

API REST simple para crear, listar, actualizar y eliminar tareas.

## Uso
```
pip install -r requirements.txt
python -m unittest -v
python app.py
```
Servidor en http://localhost:5000/tareas

## Endpoints
- GET /tareas
- POST /tareas  {"titulo": "..."}
- PUT /tareas/<id>
- DELETE /tareas/<id>
