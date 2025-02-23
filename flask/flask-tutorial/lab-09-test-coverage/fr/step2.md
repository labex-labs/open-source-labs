# Configuration et Fixtures

Ensuite, nous allons configurer des fixtures dans un fichier appelé `conftest.py`. Une fixture est une fonction qui est exécutée avant chaque fonction de test à laquelle elle est appliquée.

Dans cette étape, nous allons créer une base de données temporaire et la remplir avec des données pour les tests.

Voici le code à ajouter dans `tests/conftest.py` :

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
