# 设置数据库

首先，我们需要设置一个 SQLite 数据库来存储用户和帖子。SQLite 是一个方便的选择，因为它不需要单独的数据库服务器，并且是 Python 内置的。

在我们的 Flask 应用程序中，我们将创建一个到 SQLite 数据库的连接。在 Web 应用程序中，此连接通常与请求相关联，并在工作完成后关闭。

使用 `sqlite3.connect` 函数建立连接，我们使用 Flask 的特殊对象 `g` 来存储和重用该连接。

创建一个新的 Python 文件 `db.py` 并添加以下代码：

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # 检查 'g' 中是否不存在 'db'
    if 'db' not in g:
        # 建立到数据库的连接
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # 返回行为类似于字典的行
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # 从 'g' 中弹出 'db' 并在存在时关闭连接
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
