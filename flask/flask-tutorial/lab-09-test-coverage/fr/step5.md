# Tester l'authentification

Ensuite, nous allons écrire des tests pour l'authentification des utilisateurs. Ces tests garantissent que les utilisateurs peuvent se connecter et se déconnecter comme prévu, et que des messages d'erreur appropriés sont affichés si nécessaire.

Voici le code à ajouter dans `tests/test_auth.py` :

```python
# tests/test_auth.py

import pytest
from flask import g, session
from flaskr.db import get_db

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'
```
