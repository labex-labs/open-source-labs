# Тестирование блоговых постов

Наконец, мы напишем тесты для блоговых постов. Эти тесты гарантируют, что пользователи могут создавать, обновлять и удалять блоговые посты как ожидается.

Вот код, который нужно добавить в `tests/test_blog.py`:

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
