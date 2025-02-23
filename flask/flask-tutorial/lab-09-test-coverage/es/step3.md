# Escribir Pruebas para la Fábrica

A continuación, escribiremos pruebas para la función de fábrica que es responsable de crear la aplicación Flask. Estas pruebas aseguran que la aplicación se comporte como se espera en base a la configuración que se le pasa.

Aquí está el código para agregar en `tests/test_factory.py`:

```python
# tests/test_factory.py

from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```
