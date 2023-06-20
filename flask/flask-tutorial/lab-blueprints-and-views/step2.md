# Register the Blueprint

After creating the blueprint, we need to register it with our application. This is done in the application factory function in `flaskr/__init__.py`.

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
