# 環境に基づく設定

開発、本番、テストなど、異なる環境に対して異なる設定を持つことは一般的です。Flask を使えば、環境変数に基づいて設定を切り替えることができます。`config_dev.py` という名前の新しいファイルを作成し、次のコードを追加します。

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

次のコードを持つ `config_prod.py` という別のファイルを作成します。

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

`app.py` ファイルで、以前の設定コードを次のものに置き換えます。

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

`FLASK_ENV` 環境変数は、環境を判断するために使用されます。これが `'production'` に設定されている場合、本番用の設定が読み込まれます。それ以外の場合、開発用の設定が読み込まれます。

`FLASK_ENV` 環境変数を `'production'` に設定し、Flask アプリケーションを再起動します。`http://localhost:5000` にアクセスして、本番用の設定値付きの更新されたメッセージを表示します。
