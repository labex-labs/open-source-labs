# Настройка и фикстуры

Далее, мы настроим тестовые фикстуры в файле с именем `conftest.py`. Фикстура - это функция, которая выполняется перед каждым тестовым функцией, к которой она применяется.

В этом шаге мы создадим временную базу данных и заполним ее некоторыми данными для тестирования.

Вот код, который нужно добавить в `tests/conftest.py`:

```python
# tests/conftest.py

import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```
