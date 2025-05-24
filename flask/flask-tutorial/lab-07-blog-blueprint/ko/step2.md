# Blueprint 등록

다음으로, Blueprint 를 애플리케이션에 등록합니다.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # 기존 코드 생략

    # app.register_blueprint() 를 사용하여 팩토리에서 Blueprint 를 가져와 등록합니다.
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
