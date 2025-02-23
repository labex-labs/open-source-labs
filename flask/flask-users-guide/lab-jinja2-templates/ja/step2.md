# Flask アプリケーションの作成

`app.py` という名前の新しいファイルを作成し、必要なモジュールをインポートします。

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

このコードでは、新しい Flask アプリケーションを作成し、ルート URL ("/") のルートを定義しています。ユーザーがルート URL にアクセスすると、`index()` 関数が呼び出され、`index.html` テンプレートがレンダリングされます。
