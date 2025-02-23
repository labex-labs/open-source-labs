# `Python` アプリを作成する（Docker を使用せず）

次のコマンドを実行して、単純な Python プログラムが含まれる `app.py` という名前のファイルを作成します。（コード ブロック全体をコピーして貼り付けてください）

```bash
cd ~/project
```

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

これは、Flask を使用してポート 5000 で HTTP ウェブ サーバーを公開する単純な Python アプリです。（5000 は Flask の既定のポートです）。Python や Flask にあまり詳しくない場合は心配しないでください。これらの概念は、どんな言語で書かれたアプリケーションにも適用できます。

**オプション**：Python と pip がインストールされている場合は、このアプリをローカルで実行できます。そうでない場合は、次の手順に進んでください。

```bash
$ python3 --version
$ pip3 --version
$ pip3 install flask

$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

`http://0.0.0.0:5000/` を使用して新しいブラウザ タブでアプリを開きます。

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
