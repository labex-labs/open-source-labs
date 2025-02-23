# クロスサイトスクリプティング (XSS)

クロスサイトスクリプティング (XSS) は、攻撃者がユーザーが閲覧する Web ページに悪意のあるスクリプトを注入できる脆弱性です。Flask で XSS 攻撃を防止するには、次のガイドラインに従います。

- 常にテキストをエスケープして、任意の HTML タグの含まれないようにします。
- Jinja2 テンプレートの助けを借りずに HTML を生成する際は注意してください。
- `Markup` クラスを使用して、ユーザーが送信したデータをエスケープします。
- アップロードされたファイルから HTML またはテキストファイルを送信しないでください。

サンプルコード:

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

コードを実行するには、`app.py` という名前のファイルに保存し、`flask run` コマンドを実行します。
