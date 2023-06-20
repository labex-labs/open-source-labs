# Register the Blueprint

To use the Blueprint in your Flask application, you need to register it with the application. In the factory function of your Flask application, import the Blueprint module and register it using the `app.register_blueprint()` function.

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
