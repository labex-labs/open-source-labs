# Регистрация в приложении

Функции `close_db` и `init_db_command` должны быть зарегистрированы с экземпляром приложения, чтобы приложение могло ими пользоваться. Поскольку мы используем фабричную функцию, мы напишем функцию, которая принимает приложение и выполняет регистрацию.

Добавьте следующую функцию в файл `db.py`:

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Затем импортируйте и вызовите эту функцию из фабрики. Добавьте следующий код в файл `__init__.py`:

```python
# flaskr/__init__.py

def create_app():
    app =...
    # существующий код опущен

    from. import db
    db.init_app(app)

    return app
```
