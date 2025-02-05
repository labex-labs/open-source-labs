# 测试数据库连接

在测试工厂函数之后，我们将测试数据库连接。这些测试可确保数据库连接按预期建立和关闭。

以下是要添加到 `tests/test_db.py` 中的代码：

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
