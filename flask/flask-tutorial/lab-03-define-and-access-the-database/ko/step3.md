# 데이터베이스 초기화

다음으로, 테이블을 생성하기 위해 SQL 명령을 실행하는 Python 함수를 추가합니다. 다음 함수를 `db.py` 파일에 추가합니다.

```python
# flaskr/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
