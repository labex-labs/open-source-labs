# インスタンス フォルダ

Flask は、特定の展開に固有の設定ファイルを格納するためのインスタンス フォルダを提供します。これにより、展開に固有の設定をコードの残りの部分から分離することができます。デフォルトでは、Flask はアプリケーションと同じディレクトリに `instance` という名前のフォルダを使用します。

`app.py` ファイルと同じディレクトリに `instance` という名前の新しいフォルダを作成します。`instance` フォルダ内に `config.cfg` という名前のファイルを作成し、次のコードを追加します。

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

`app.py` ファイルで、設定コードの前に次のコードを追加します。

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

`instance_path` は `instance` フォルダの絶対パスに設定されます。`from_pyfile` メソッドは、インスタンス フォルダ内の `config.cfg` ファイルから設定を読み込みます。

Flask アプリケーションを再起動し、`http://localhost:5000` にアクセスして、インスタンス設定値付きの更新されたメッセージを表示します。
