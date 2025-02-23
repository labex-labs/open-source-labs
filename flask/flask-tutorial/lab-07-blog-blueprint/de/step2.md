# Registriere das Blueprint

Als nächstes registrieren wir das Blueprint in unserer Anwendung.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # vorhandener Code weggelassen

    # importiere und registriere das Blueprint aus der Factory mit app.register_blueprint()
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
