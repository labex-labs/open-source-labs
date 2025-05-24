# Testar as Publicações do Blog

Finalmente, escreveremos testes para as publicações do blog. Estes testes garantem que os usuários podem criar, atualizar e excluir publicações do blog conforme o esperado.

Aqui está o código a ser adicionado em `tests/test_blog.py`:

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
