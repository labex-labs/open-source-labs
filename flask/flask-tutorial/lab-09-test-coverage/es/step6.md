# Pruebas de Publicaciones del Blog

Finalmente, escribiremos pruebas para las publicaciones del blog. Estas pruebas aseguran que los usuarios puedan crear, actualizar y eliminar publicaciones del blog como se espera.

Aquí está el código para agregar en `tests/test_blog.py`:

```python
# tests/test_blog.py

import pytest
from flaskr.db import get_db

def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2
```
