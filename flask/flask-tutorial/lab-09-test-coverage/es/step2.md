# Configuración y Fixtures

A continuación, configuraremos fixtures en un archivo llamado `conftest.py`. Una fixture es una función que se ejecuta antes de cada función de prueba a la que se aplica.

En este paso, crearemos una base de datos temporal y la llenaremos con algunos datos para las pruebas.

Aquí está el código para agregar en `tests/conftest.py`:

```python
# tests/conftest.py

import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```
