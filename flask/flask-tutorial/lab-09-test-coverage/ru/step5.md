# Тестирование аутентификации

Далее, мы напишем тесты для аутентификации пользователей. Эти тесты гарантируют, что пользователи могут входить и выходить из системы как ожидается, и что при необходимости отображаются соответствующие сообщения об ошибках.

Вот код, который нужно добавить в `tests/test_auth.py`:

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
