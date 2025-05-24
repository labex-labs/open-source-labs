# 설정 및 Fixtures (고정 장치)

다음으로, `conftest.py`라는 파일에 테스트 fixture (고정 장치) 를 설정합니다. Fixture (고정 장치) 는 적용되는 각 테스트 함수 전에 실행되는 함수입니다.

이 단계에서는 임시 데이터베이스를 생성하고 테스트를 위해 일부 데이터를 채웁니다.

`tests/conftest.py`에 추가할 코드는 다음과 같습니다.

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
