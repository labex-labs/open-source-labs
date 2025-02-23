# Registrar el Blueprint

A continuación, registraremos el blueprint con nuestra aplicación.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # código existente omitido

    # importa y registra el blueprint desde la fábrica usando app.register_blueprint()
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
