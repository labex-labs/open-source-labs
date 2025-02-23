# アプリケーションに登録する

`close_db` 関数と `init_db_command` 関数は、アプリケーションが使用できるようにアプリケーションインスタンスに登録する必要があります。ファクトリ関数を使用しているため、アプリケーションを受け取り、登録を行う関数を書きます。

`db.py` ファイルに次の関数を追加します。

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

その後、ファクトリからこの関数をインポートして呼び出します。`__init__.py` ファイルに次のコードを追加します。

```python
# flaskr/__init__.py

def create_app():
    app =...
    # 既存のコードは省略
    from. import db
    db.init_app(app)

    return app
```
