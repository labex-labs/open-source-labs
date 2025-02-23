# Docker イメージを作成して構築する

では、ローカルに Python がインストールされていない場合どうなるでしょうか？心配しないでください！コンテナを使用する利点の 1 つは、ホスト マシンに Python をインストールすることなく、コンテナ内で Python を構築できることです。

次のコマンドを実行して `Dockerfile` を作成します。（コード ブロック全体をコピーして貼り付けてください）

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Dockerfile には、Docker イメージを構築するために必要な指示が記載されています。上記のファイルを 1 行ずつ見ていきましょう。

**FROM python:3.8-alpine**
これは、Dockerfile の起点です。すべての Dockerfile は、レイヤーを構築するための起点イメージとなる `FROM` 行から始まる必要があります。

この場合、私たちは `python:3.8-alpine` ベース レイヤーを選択しています（[python3.8/alpine3.12 の Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) を参照）。なぜなら、このレイヤーには既にアプリケーションを実行するために必要な Python と pip のバージョンが含まれているからです。

`alpine` バージョンは、[Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux) ディストリビューションを使用しています。これは、他の多くの Linux のフレーバーよりも大幅に小さく、サイズが約 8MB です。一方、ディスクへの最小インストールサイズは約 130MB です。小さなイメージは、ダウンロード（展開）がはるかに速くなり、攻撃面が小さいためセキュリティ上の利点もあります。[Alpine Linux](https://alpinelinux.org/downloads/) は、musl と BusyBox に基づく Linux ディストリビューションです。

ここでは、Python イメージに対して "3.8-alpine" タグを使用しています。[Docker Hub](https://hub.docker.com/_/python/) の公式 Python イメージの利用可能なタグを確認してください。親イメージを継承する際には、特定のタグを使用することがベスト プラクティスです。これにより、親依存関係の変更を制御できます。タグが指定されていない場合、"latest" タグが有効になります。これは、イメージの最新バージョンを指す動的ポインタとして機能します。

セキュリティ上の理由から、Docker イメージを構築するためのベースとなるレイヤーを理解することは非常に重要です。そのため、[docker hub](https://hub.docker.com/) にある "公式" イメージ、または docker-store にある非コミュニティ イメージのみを使用することを強くお勧めします。これらのイメージは、特定のセキュリティ要件を満たすように検証されており、ユーザーが追うのに非常に良いドキュメントも備えています。[docker hub](https://hub.docker.com) では、この [Python ベース イメージ](https://hub.docker.com/_/python) や他に使用できるすべてのイメージに関する詳細情報を見つけることができます。

より複雑なアプリケーションの場合、チェーンの上位にある `FROM` イメージを使用する必要がある場合があります。たとえば、私たちの Python アプリの親 [Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) は `FROM alpine` から始まり、その後、イメージに対する一連の `CMD` と `RUN` コマンドを指定しています。もっと細かい制御が必要な場合は、`FROM alpine`（または別のディストリビューション）から始めて、それらの手順を自分で実行することができます。最初は、必要に合わせた公式イメージを使用することをお勧めします。

**RUN pip install flask**
`RUN` コマンドは、アプリケーション用にイメージをセットアップするために必要なコマンドを実行します。たとえば、パッケージのインストール、ファイルの編集、またはファイルのパーミッションの変更などです。この場合、私たちは flask をインストールしています。`RUN` コマンドはビルド時に実行され、イメージのレイヤーに追加されます。

**CMD ["python","app.py"]**
`CMD` は、コンテナを起動したときに実行されるコマンドです。ここでは、`CMD` を使用して Python アプリを実行しています。

Dockerfile には 1 つの `CMD` のみが許されます。複数の `CMD` を指定した場合、最後の `CMD` が有効になります。親の python:3.8-alpine も `CMD` (`CMD python3`) を指定しています。公式 python:alpine イメージの Dockerfile は [ここ](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) にあります。

ホストに Python をインストールすることなく、公式の Python イメージを直接使用して Python スクリプトを実行することができます。しかし、今日は、ソースを含めたカスタム イメージを作成しています。これにより、アプリケーション付きのイメージを構築し、他の環境に配布することができます。

**COPY app.py /app.py**
これは、ローカル ディレクトリ（`docker image build` を実行する場所）の app.py をイメージの新しいレイヤーにコピーします。この指示は、Dockerfile の最後の行です。頻繁に変更されるレイヤー、たとえばソース コードをイメージにコピーする場合、Docker レイヤー キャッシュの恩恵を最大限に活用するために、ファイルの下部に配置する必要があります。これにより、キャッシュされるはずのレイヤーを再構築することなく済みます。たとえば、`FROM` 指示に変更があった場合、このイメージのすべての後続レイヤーのキャッシュが無効になります。この実験の後半でこれを示します。

これを `CMD ["python","app.py"]` の行の後に置くのは直感的ではないように見えます。覚えておいてください。`CMD` の行は、コンテナが起動したときにのみ実行されるため、ここで `file not found` エラーは発生しません。

これで、非常にシンプルな Dockerfile が完成しました。Dockerfile に記載できるコマンドの完全なリストは [ここ](https://docs.docker.com/engine/reference/builder/) にあります。これで Dockerfile を定義したので、これを使ってカスタム Docker イメージを構築しましょう。

Docker イメージを構築します。

`-t` を指定して、イメージ名を `python-hello-world` にします。

```bash
docker image build -t python-hello-world.
```

イメージがイメージ一覧に表示されていることを確認します。

```bash
docker image ls
```

**注**：ベース イメージ `python:3.8-alpine` も一覧に表示されます。

イメージの履歴とそのレイヤーを表示するには、履歴コマンドを実行します。

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
