# 向应用程序注册

`close_db` 和 `init_db_command` 函数需要向应用程序实例注册，以便应用程序使用。由于我们使用的是工厂函数，我们将编写一个接受应用程序并进行注册的函数。

将以下函数添加到 `db.py` 文件中：

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

然后，从工厂函数中导入并调用此函数。将以下代码添加到 `__init__.py` 文件中：

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 省略现有代码

    from. import db
    db.init_app(app)

    return app
```
