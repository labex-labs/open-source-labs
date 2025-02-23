# Flask アプリケーションにコマンドを登録する

Flask CLI を通じてカスタムコマンドを利用できるようにするには、Flask アプリケーションにそれらを登録する必要があります。`app.py` ファイルを開き、次のように変更します。

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

ファイルを保存し、`flask run` コマンドを使って Flask 開発サーバーを再起動します。これで、コマンドラインからカスタムコマンド `greet` を実行できるようになります。

```
flask greet John
```

ターミナルに「Hello, John!」というメッセージが表示されるはずです。
