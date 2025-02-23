# Tester la connexion à la base de données

Après avoir testé la factory, nous allons tester la connexion à la base de données. Ces tests garantissent que la connexion à la base de données est établie et fermée comme prévu.

Voici le code à ajouter dans `tests/test_db.py` :

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
