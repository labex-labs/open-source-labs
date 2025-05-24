# Testar a Conexão ao Banco de Dados

Após testar a _factory_, testaremos a conexão ao banco de dados. Estes testes garantem que a conexão ao banco de dados seja estabelecida e fechada conforme o esperado.

Aqui está o código a ser adicionado em `tests/test_db.py`:

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
