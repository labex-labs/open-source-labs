# Teste die Datenbankverbindung

Nachdem wir die Factory getestet haben, werden wir die Datenbankverbindung testen. Diese Tests gewährleisten, dass die Datenbankverbindung wie erwartet hergestellt und geschlossen wird.

Hier ist der Code, den Sie in `tests/test_db.py` hinzufügen sollten:

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
