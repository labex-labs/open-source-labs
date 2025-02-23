# Enregistrer le blueprint

Après avoir créé le blueprint, nous devons l'enregistrer avec notre application. Cela se fait dans la fonction de fabrique d'application dans `flaskr/__init__.py`.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # code existant omis

    # Importez et enregistrez le blueprint
    from. import auth
    app.register_blueprint(auth.bp)

    return app
```
