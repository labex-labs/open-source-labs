# 测试认证

接下来，我们将编写用户认证的测试。这些测试可确保用户能够按预期登录和注销，并且在必要时显示适当的错误消息。

以下是要添加到 `tests/test_auth.py` 中的代码：

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
