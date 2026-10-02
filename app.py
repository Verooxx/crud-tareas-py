from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = []
siguiente_id = 1


@app.get("/tareas")
def listar():
    return jsonify(tareas)


@app.post("/tareas")
def crear():
    global siguiente_id
    datos = request.get_json(silent=True) or {}
    titulo = datos.get("titulo")
    if not titulo:
        return jsonify({"error": "El título es obligatorio"}), 400
    if len(titulo.strip()) < 3:
        return jsonify({"error": "El título debe tener al menos 3 caracteres"}), 400
    tarea = {"id": siguiente_id, "titulo": titulo, "completada": False}
    siguiente_id += 1
    tareas.append(tarea)
    return jsonify(tarea), 201


@app.put("/tareas/<int:tarea_id>")
def actualizar(tarea_id):
    datos = request.get_json(silent=True) or {}
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea.update({k: v for k, v in datos.items() if k != "id"})
            return jsonify(tarea)
    return jsonify({"error": "No encontrada"}), 404


@app.delete("/tareas/<int:tarea_id>")
def eliminar(tarea_id):
    global tareas
    tareas = [t for t in tareas if t["id"] != tarea_id]
    return "", 204


if __name__ == "__main__":
    app.run(port=5000, debug=True)