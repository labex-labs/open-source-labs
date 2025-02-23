# 変更を展開する

「ハローワールド！」アプリケーションは評価が過大です。代わりに「ハロービューティフルワールド！」と表示するようにアプリを更新しましょう。

## `app.py` を更新する

`app.py` の中で、文字列「Hello World」を「Hello Beautiful World!」に置き換えます。次のコマンドでファイルを更新できます。（コード ブロック全体をコピーして貼り付けてください）

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## イメージを再構築してプッシュする

アプリが更新されたので、上記の手順を繰り返してアプリを再構築し、Docker Hub レジストリにプッシュする必要があります。

まず再構築します。今回は、ビルド コマンドで Docker Hub のユーザー名を使用します。

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world.
```

ステップ 1 - 3 における「キャッシュの使用」に注目してください。Docker イメージのこれらのレイヤーは既に構築されており、`docker image build` は再構築する代わりにキャッシュからこれらのレイヤーを使用します。

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

レイヤーをプッシュするためのキャッシュ メカニズムもあります。Docker Hub には、以前のプッシュからのレイヤーのうち、1 つを除くすべてが既にあります。したがって、変更された 1 つのレイヤーのみがプッシュされます。

レイヤーを変更すると、その上に構築されたすべてのレイヤーを再構築する必要があります。Dockerfile の各行は、その前の行から作成されたレイヤーの上に構築される新しいレイヤーを作成します。これが、Dockerfile の行の順序が重要な理由です。私たちは Dockerfile を最適化して、最も変更される可能性のあるレイヤー（`COPY app.py /app.py`）が Dockerfile の最後の行になるようにしました。一般的にアプリケーションの場合、コードが最も頻繁に変更されます。この最適化は、自動化をできるだけ早く実行したい CI/CD プロセスにとって特に重要です。
