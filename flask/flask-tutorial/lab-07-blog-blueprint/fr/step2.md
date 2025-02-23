# Enregistrer le Blueprint

Ensuite, nous allons enregistrer le blueprint avec notre application.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # code existant omis

    # importer et enregistrer le blueprint à partir de la fabrique en utilisant app.register_blueprint()
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
