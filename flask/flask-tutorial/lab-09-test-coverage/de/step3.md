# Schreibe Tests für die Factory

Als nächstes werden wir Tests für die Factory-Funktion schreiben, die für das Erstellen der Flask-Anwendung verantwortlich ist. Diese Tests gewährleisten, dass die Anwendung sich gemäß der übergebenen Konfiguration so verhält, wie erwartet.

Hier ist der Code, den Sie in `tests/test_factory.py` hinzufügen sollten:

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
