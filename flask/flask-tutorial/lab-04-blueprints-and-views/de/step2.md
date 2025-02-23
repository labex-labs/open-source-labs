# Registrieren des Blueprints

Nachdem das Blueprint erstellt wurde, müssen wir es mit unserer Anwendung registrieren. Dies geschieht in der Anwendungsfabrikfunktion in `flaskr/__init__.py`.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # vorhandener Code weggelassen

    # Importieren und Registrieren des Blueprints
    from. import auth
    app.register_blueprint(auth.bp)

    return app
```
