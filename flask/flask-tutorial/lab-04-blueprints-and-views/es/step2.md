# Registrar el blueprint

Después de crear el blueprint, debemos registrarlo con nuestra aplicación. Esto se hace en la función de fábrica de la aplicación en `flaskr/__init__.py`.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # código existente omitido

    # Importa y registra el blueprint
    from. import auth
    app.register_blueprint(auth.bp)

    return app
```
