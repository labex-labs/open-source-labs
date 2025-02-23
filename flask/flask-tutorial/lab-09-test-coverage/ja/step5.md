# 認証のテスト

次に、ユーザー認証のテストを作成します。これらのテストは、ユーザーが期待通りにログインおよびログアウトできること、および必要に応じて適切なエラーメッセージが表示されることを確認します。

`tests/test_auth.py` に追加するコードは以下の通りです。

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
