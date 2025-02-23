# セットアップとフィクスチャ

次に、`conftest.py` という名前のファイルにテストフィクスチャをセットアップします。フィクスチャは、適用される各テスト関数の前に実行される関数です。

このステップでは、一時的なデータベースを作成し、テスト用のデータを格納します。

`tests/conftest.py` に追加するコードは以下の通りです。

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
