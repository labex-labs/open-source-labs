# クロスサイトリクエストフォージェリ (CSRF)

クロスサイトリクエストフォージェリ (CSRF) は、ユーザーに対してウェブサイト上で意図しない操作を実行させる攻撃です。Flask で CSRF 攻撃を防止するには、次のガイドラインに従います。

- サーバーコンテンツを変更する要求を検証するために、ワンタイムトークンを使用します。
- トークンをクッキーに保存し、フォームデータとともに送信します。
- サーバーで受け取ったトークンと、クッキーに保存されたトークンを比較します。

サンプルコード：

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Delete user profile
            return redirect(url_for('index'))
    return 'Invalid request'

if __name__ == '__main__':
    app.run()
```

コードを実行するには、`app.py` という名前のファイルに保存し、`flask run` コマンドを実行します。
