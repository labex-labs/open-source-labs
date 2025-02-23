# Écrire des tests pour la factory

Ensuite, nous allons écrire des tests pour la fonction factory qui est responsable de la création de l'application Flask. Ces tests garantissent que l'application se comporte comme prévu en fonction de la configuration qui lui est passée.

Voici le code à ajouter dans `tests/test_factory.py` :

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
