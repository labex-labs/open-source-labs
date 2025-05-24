# 인증 테스트

다음으로, 사용자 인증에 대한 테스트를 작성합니다. 이러한 테스트는 사용자가 예상대로 로그인 및 로그아웃할 수 있는지, 그리고 필요한 경우 적절한 오류 메시지가 표시되는지 확인합니다.

`tests/test_auth.py`에 추가할 코드는 다음과 같습니다.

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
