import unittest

import app as modulo


class TestTareas(unittest.TestCase):
    def setUp(self):
        modulo.tareas.clear()
        modulo.siguiente_id = 1
        self.cliente = modulo.app.test_client()

    def test_crear_y_listar(self):
        r = self.cliente.post("/tareas", json={"titulo": "Estudiar"})
        self.assertEqual(r.status_code, 201)
        lista = self.cliente.get("/tareas").get_json()
        self.assertEqual(len(lista), 1)

    def test_titulo_obligatorio(self):
        r = self.cliente.post("/tareas", json={})
        self.assertEqual(r.status_code, 400)

    def test_titulo_muy_corto(self):
        r = self.cliente.post("/tareas", json={"titulo": "ab"})
        self.assertEqual(r.status_code, 400)

    def test_actualizar(self):
        self.cliente.post("/tareas", json={"titulo": "Estudiar"})
        r = self.cliente.put("/tareas/1", json={"completada": True})
        self.assertTrue(r.get_json()["completada"])

    def test_eliminar(self):
        self.cliente.post("/tareas", json={"titulo": "Estudiar"})
        self.cliente.delete("/tareas/1")
        self.assertEqual(self.cliente.get("/tareas").get_json(), [])

    def test_eliminar_inexistente(self):
        r = self.cliente.delete("/tareas/99")
        self.assertEqual(r.status_code, 404)

if __name__ == "__main__":
    unittest.main()