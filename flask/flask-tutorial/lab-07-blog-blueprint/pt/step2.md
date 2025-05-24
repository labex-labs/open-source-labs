# Registrar Blueprint (Blueprint)

Em seguida, vamos registrar o blueprint com a nossa aplicação.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    # import and register the blueprint from the factory using app.register_blueprint()
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
