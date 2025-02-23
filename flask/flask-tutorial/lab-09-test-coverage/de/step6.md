# Teste Blog-Beiträge

Schließlich werden wir Tests für Blog-Beiträge schreiben. Diese Tests gewährleisten, dass Benutzer Blog-Beiträge wie erwartet erstellen, aktualisieren und löschen können.

Hier ist der Code, den Sie in `tests/test_blog.py` hinzufügen sollten:

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
