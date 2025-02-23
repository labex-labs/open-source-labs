# アプリケーションファクトリのセットアップ

次に、`flaskr` ディレクトリに `__init__.py` ファイルを作成します。このファイルは 2 つの目的を果たします。アプリケーションファクトリを含み、Python に対して `flaskr` ディレクトリをパッケージとして扱うべきであることを示します。

`__init__.py` ファイルでは、必要なモジュールをインポートし、アプリケーションをインスタンス化して構成する `create_app()` 関数を定義します。

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ここに追加するコードが増えます...

    return app
```
