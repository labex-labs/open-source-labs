# Setup und Fixtures

Als nächstes werden wir Test-Fixtures in einer Datei namens `conftest.py` einrichten. Eine Fixture ist eine Funktion, die vor jeder Testfunktion ausgeführt wird, auf die sie angewendet wird.

In diesem Schritt werden wir eine temporäre Datenbank erstellen und sie mit einigen Daten für das Testing befüllen.

Hier ist der Code, den Sie in `tests/conftest.py` hinzufügen sollten:

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
