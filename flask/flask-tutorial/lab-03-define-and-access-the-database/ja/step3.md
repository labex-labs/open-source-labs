# データベースの初期化

次に、テーブルを作成するためのSQLコマンドを実行するPython関数を追加します。`db.py` ファイルに次の関数を追加します。

```python
# flaskr/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
