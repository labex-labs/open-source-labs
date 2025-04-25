# Set-Cookie オプション

Flask でクッキーを設定する際には、機密データを保護するためのセキュリティオプションを考慮することが重要です。推奨されるオプションのいくつかは以下の通りです。

- Secure：クッキーを HTTPS トラフィックに限定します。
- HttpOnly：クッキーの内容を JavaScript で読み取られることから保護します。
- SameSite：外部サイトからの要求でクッキーがどのように送信されるかを制限します。

サンプルコード：

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

コードを実行するには、`app.py` という名前のファイルに保存し、`flask run` コマンドを実行します。
