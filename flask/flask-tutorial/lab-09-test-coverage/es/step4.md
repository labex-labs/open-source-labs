# Prueba de la Conexión a la Base de Datos

Después de probar la fábrica, probaremos la conexión a la base de datos. Estas pruebas aseguran que la conexión a la base de datos se establece y cierra como se espera.

Aquí está el código para agregar en `tests/test_db.py`:

```python
# tests/test_db.py

import sqlite3
import pytest
from flaskr.db import get_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```
