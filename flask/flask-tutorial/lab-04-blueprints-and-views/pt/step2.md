# Registrar o Blueprint (Planta)

Após criar o blueprint (planta), precisamos registrá-lo com nossa aplicação. Isso é feito na função da fábrica da aplicação em `flaskr/__init__.py`.

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
