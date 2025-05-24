# 블로그 게시물 테스트

마지막으로, 블로그 게시물에 대한 테스트를 작성합니다. 이러한 테스트는 사용자가 예상대로 블로그 게시물을 생성, 업데이트 및 삭제할 수 있는지 확인합니다.

`tests/test_blog.py`에 추가할 코드는 다음과 같습니다.

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
