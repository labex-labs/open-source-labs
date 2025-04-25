# データベースのセットアップ

まず、ユーザーと投稿を保存するための SQLite データベースをセットアップする必要があります。SQLite は、別個のデータベースサーバーを必要とせず、Python に組み込まれているため便利な選択肢です。

私たちの Flask アプリケーションでは、SQLite データベースへの接続を作成します。この接続は通常、Web アプリケーションの要求に関連付けられ、作業が完了した後に閉じられます。

接続は `sqlite3.connect` 関数を使用して確立され、Flask の特殊オブジェクト `g` を使用して接続を保存および再利用します。

新しい Python ファイル `db.py` を作成し、次のコードを追加します。

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # 'db' が 'g' にないことを確認する
    if 'db' not in g:
        # データベースへの接続を確立する
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # 辞書のように振る舞う行を返す
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # 'g' から 'db' を削除し、存在する場合は接続を閉じる
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
