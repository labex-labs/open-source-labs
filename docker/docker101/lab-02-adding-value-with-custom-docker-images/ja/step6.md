# イメージ レイヤーの理解

Docker の主な設計特性の 1 つは、ユニオン ファイル システムの使用です。

先ほど作成した `Dockerfile` を見てみましょう。

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

これらの各行は 1 つのレイヤーです。各レイヤーには、その前のレイヤーとの差分、diff または変更点のみが含まれています。これらのレイヤーを単一の実行中のコンテナにまとめるために、Docker は `ユニオン ファイル システム` を使用して、レイヤーを透明に重ねて単一のビューにします。

イメージの各レイヤーは `読み取り専用` ですが、実行中のコンテナ用に作成される最上位のレイヤーを除いています。読み取り/書き込み可能なコンテナ レイヤーは「書き込み時コピー」を実装しており、これは、下位のイメージ レイヤーに格納されているファイルが、それらのファイルに編集が加えられるときにのみ読み取り/書き込み可能なコンテナ レイヤーに引き上げられることを意味します。その後、これらの変更は実行中のコンテナ レイヤーに格納されます。「書き込み時コピー」機能は非常に高速で、ほとんどの場合、パフォーマンスに顕著な影響を与えません。`docker diff` コマンドを使用することで、コンテナ レベルに引き上げられたファイルを確認することができます。`docker diff` の使用方法に関する詳細は、[ここ](https://docs.docker.com/engine/reference/commandline/diff/) で見つけることができます。

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

イメージ レイヤーは `読み取り専用` であるため、イメージと実行中のコンテナによって共有することができます。たとえば、同じベース レイヤーを持つ独自の Dockerfile で新しい Python アプリを作成すると、最初の Python アプリと共通のすべてのレイヤーを共有します。

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

同じイメージから複数のコンテナを起動する場合も、レイヤーの共有を体験することができます。コンテナは同じ読み取り専用レイヤーを使用するため、コンテナの起動は非常に高速で、ホスト上の占有領域も非常に小さいことが想像できます。

この Dockerfile と、この実験で先ほど作成した Dockerfile には重複する行があることに気付くかもしれません。これは非常に単純な例ですが、両方の Dockerfile の共通の行を「ベース」Dockerfile にまとめることができます。その後、各子 Dockerfile で `FROM` コマンドを使用してそれを指定することができます。

イメージのレイヤリングにより、ビルドとプッシュのための Docker キャッシュ メカニズムが可能になります。たとえば、最後の `docker push` の出力を見ると、イメージの一部のレイヤーが既に Docker Hub に存在することがわかります。

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

レイヤーをもっと詳細に見るには、作成した Python イメージの `docker image history` コマンドを使用することができます。

```bash
$ docker image history python-hello-world
```

各行はイメージの 1 つのレイヤーを表します。上位の行が先ほど作成した Dockerfile に一致し、その下の行は親の Python イメージから引き継がれていることに気付くでしょう。「<欠落>」タグは心配しないでください。これらはまだ通常のレイヤーです。ただし、docker システムによって ID が付けられていないだけです。
