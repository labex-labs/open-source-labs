# Tester les articles de blog

Enfin, nous allons écrire des tests pour les articles de blog. Ces tests garantissent que les utilisateurs peuvent créer, mettre à jour et supprimer des articles de blog comme prévu.

Voici le code à ajouter dans `tests/test_blog.py` :

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
