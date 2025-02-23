# Prueba de la Autenticación

A continuación, escribiremos pruebas para la autenticación de usuarios. Estas pruebas aseguran que los usuarios puedan iniciar sesión y cerrar sesión como se espera, y que se muestren los mensajes de error adecuados cuando sea necesario.

Aquí está el código para agregar en `tests/test_auth.py`:

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
