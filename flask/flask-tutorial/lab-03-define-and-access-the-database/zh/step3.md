# 初始化数据库

接下来，我们将添加 Python 函数来运行创建表的 SQL 命令。将以下函数添加到 `db.py` 文件中：

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
