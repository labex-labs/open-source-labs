# Flask アプリケーションの作成

`app.py` という名前の新しい Python ファイルを作成し、次のコードを追加して基本的な Flask アプリケーションを作成します。

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

ファイルを保存し、ターミナルで次のコマンドを使用して実行します。

```
python app.py
```
