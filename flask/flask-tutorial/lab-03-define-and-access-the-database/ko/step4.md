# 애플리케이션에 등록

`close_db` 및 `init_db_command` 함수는 애플리케이션에서 사용하기 위해 애플리케이션 인스턴스에 등록되어야 합니다. 팩토리 함수를 사용하고 있으므로, 애플리케이션을 인수로 받아 등록을 수행하는 함수를 작성합니다.

다음 함수를 `db.py` 파일에 추가합니다.

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

그런 다음, 팩토리에서 이 함수를 가져와 호출합니다. 다음 코드를 `__init__.py` 파일에 추가합니다.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```
