# Flask アプリケーションのセットアップ

開発サーバを実行する前に、Flask アプリケーションをセットアップする必要があります。`app.py` という名前の新しい Python ファイルを作成し、次のコードを追加します。

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

このコードでは、Flask アプリケーションを作成し、単純な "Hello, Flask!" メッセージを返すルートを定義しています。`if __name__ == "__main__":` ブロックは、Flask アプリケーションがスクリプトが直接実行されたときにのみ実行され、モジュールとしてインポートされたときには実行されないことを保証します。
