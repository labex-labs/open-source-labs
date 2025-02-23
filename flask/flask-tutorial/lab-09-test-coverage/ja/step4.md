# データベース接続のテスト

ファクトリ関数のテストの後、データベース接続をテストします。これらのテストは、データベース接続が期待通りに確立され、閉じられることを確認します。

`tests/test_db.py` に追加するコードは以下の通りです。

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
