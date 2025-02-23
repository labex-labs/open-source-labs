# 基本設定

次に、Flask アプリケーションにいくつかの基本設定を追加しましょう。同じ `app.py` ファイルに、次のコードを追加します。

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

`DEBUG` 設定はデバッグモードを有効にし、開発中に役立つエラーメッセージを提供します。`SECRET_KEY` 設定は、セッションクッキーの安全な署名付けやその他のセキュリティ関連のニーズに使用されます。

設定値にアクセスするには、`app.config` 辞書を使用できます。たとえば、`SECRET_KEY` の値を表示するには、`hello` ルートに次のコードを追加します。

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Flask アプリケーションを再起動し、`http://localhost:5000` にアクセスして、シークレットキー付きの更新されたメッセージを表示します。
