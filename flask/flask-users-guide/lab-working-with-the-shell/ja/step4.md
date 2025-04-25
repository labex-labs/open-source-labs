# シェルの使いやすさの向上

シェルの使いやすさを向上させるには、ヘルパーメソッドを持つモジュール (`shelltools.py`) を作成し、これをインタラクティブセッションにインポートできるようにします。このモジュールには、データベースの初期化やテーブルの削除などのタスクに対する追加のヘルパーメソッドを含めることができます。

```python
# File: shelltools.py

def initialize_database():
    # データベースを初期化するコード
    pass

def drop_tables():
    # テーブルを削除するコード
    pass
```

インタラクティブシェルでは、`shelltools` モジュールから必要なメソッドをインポートします。

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# shelltools モジュールから必要なメソッドをインポート
from shelltools import *

# インポートしたメソッドを使用
initialize_database()
drop_tables()
```
