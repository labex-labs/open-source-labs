# Teste die Authentifizierung

Als nächstes werden wir Tests für die Benutzerauthentifizierung schreiben. Diese Tests gewährleisten, dass Benutzer sich wie erwartet einloggen und ausloggen können und dass bei Bedarf entsprechende Fehlermeldungen angezeigt werden.

Hier ist der Code, den Sie in `tests/test_auth.py` hinzufügen sollten:

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
