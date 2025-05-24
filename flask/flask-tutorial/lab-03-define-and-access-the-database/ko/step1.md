# 데이터베이스 설정

먼저, 사용자 및 게시물을 저장하기 위해 SQLite 데이터베이스를 설정해야 합니다. SQLite 는 별도의 데이터베이스 서버가 필요 없고 Python 에 내장되어 있어 편리한 선택입니다.

Flask 애플리케이션에서 SQLite 데이터베이스에 대한 연결을 생성합니다. 이 연결은 일반적으로 웹 애플리케이션에서 요청에 연결되며, 작업이 완료된 후 닫힙니다.

연결은 `sqlite3.connect` 함수를 사용하여 설정하며, Flask 의 특수 객체 `g`를 사용하여 연결을 저장하고 재사용합니다.

새로운 Python 파일 `db.py`를 생성하고 다음 코드를 추가합니다.

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # Check if 'db' is not in 'g'
    if 'db' not in g:
        # Establish a connection to the database
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Pop 'db' from 'g' and close the connection if it exists
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
