# Testar a Autenticação

Em seguida, escreveremos testes para a autenticação do usuário. Estes testes garantem que os usuários podem fazer login e logout conforme o esperado, e que as mensagens de erro apropriadas são exibidas quando necessário.

Aqui está o código a ser adicionado em `tests/test_auth.py`:

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
