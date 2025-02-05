# 设置与夹具

接下来，我们将在名为 `conftest.py` 的文件中设置测试夹具。夹具是一个函数，在应用它的每个测试函数之前运行。

在这一步中，我们将创建一个临时数据库，并用一些数据填充它以进行测试。

以下是要添加到 `tests/conftest.py` 中的代码：

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
