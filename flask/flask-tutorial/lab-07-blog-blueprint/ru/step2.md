# Регистрация Blueprint

Далее мы зарегистрируем Blueprint в нашем приложении.

```python
# flaskr/__init__.py

def create_app():
    app =...
    # существующий код опущен

    # импортируем и регистрируем Blueprint из фабрики с использованием app.register_blueprint()
    from. import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
