# ブログ投稿のテスト

最後に、ブログ投稿のテストを作成します。これらのテストは、ユーザーが期待通りにブログ投稿を作成、更新、および削除できることを確認します。

`tests/test_blog.py` に追加するコードは以下の通りです。

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
