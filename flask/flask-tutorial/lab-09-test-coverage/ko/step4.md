# 데이터베이스 연결 테스트

Factory (팩토리) 테스트 후, 데이터베이스 연결을 테스트합니다. 이러한 테스트는 데이터베이스 연결이 예상대로 설정되고 닫히는지 확인합니다.

`tests/test_db.py`에 추가할 코드는 다음과 같습니다.

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
