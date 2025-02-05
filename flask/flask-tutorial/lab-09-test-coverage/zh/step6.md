# 测试博客文章

最后，我们将编写博客文章的测试。这些测试可确保用户能够按预期创建、更新和删除博客文章。

以下是要添加到 `tests/test_blog.py` 中的代码：

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
