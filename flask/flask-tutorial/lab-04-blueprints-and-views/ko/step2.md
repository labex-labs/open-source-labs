# 블루프린트 등록

블루프린트를 생성한 후에는 애플리케이션에 등록해야 합니다. 이는 `flaskr/__init__.py`의 애플리케이션 팩토리 함수에서 수행됩니다.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    # Import and register the blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
