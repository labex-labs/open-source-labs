# Тестирование соединения с базой данных

После тестирования фабрики мы проверим соединение с базой данных. Эти тесты гарантируют, что соединение с базой данных устанавливается и закрывается как ожидается.

Вот код, который нужно добавить в `tests/test_db.py`:

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
