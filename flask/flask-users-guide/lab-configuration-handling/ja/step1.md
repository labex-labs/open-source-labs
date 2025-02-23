# Flask アプリケーションを作成する

まず、基本的な Flask アプリケーションを作成しましょう。`app.py` という名前のファイルを作成し、次のコードを追加します。

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

アプリケーションを実行するには、ターミナルで次のコマンドを実行します。

```shell
python app.py
```

Web ブラウザを開き、`http://localhost:5000` にアクセスして、「Hello, Flask!」のメッセージを表示します。
