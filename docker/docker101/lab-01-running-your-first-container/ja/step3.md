# 複数のコンテナを実行する

## Docker Hub を探索する

[Docker Hub](https://hub.docker.com/explore/) は、Docker イメージの公開中央レジストリであり、コミュニティおよび公式イメージが含まれています。

イメージを検索する際には、「Docker Certified」、「Verified Publisher」、「公式イメージ」のフィルターがあります。「Docker Certified」フィルターを選択すると、エンタープライズ向けに準備され、Docker Enterprise Edition 製品でテストされたイメージが見つかります。本番環境に展開する予定の独自のイメージを作成する際には、Docker Store からの検証されていないコンテンツを使用しないようにすることが重要です。これらの検証されていないイメージには、セキュリティ上の脆弱性や、場合によっては悪意のあるソフトウェアが含まれている可能性があります。

この実験のステップ 2 では、Docker Hub からのいくつかの検証済みイメージを使用してコンテナを起動します。nginx ウェブ サーバーと mongo データベースです。

## Nginx サーバーを実行する

Docker Hub からの [公式 Nginx イメージ](https://hub.docker.com/_/nginx) を使用してコンテナを実行しましょう。

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

ここではいくつかの新しいフラグを使用しています。`--detach` フラグにより、このコンテナをバックグラウンドで実行します。`publish` フラグにより、コンテナ内のポート 80（nginx の既定のポート）を、ホスト上のポート 8080 を介して公開します。NET ネームスペースにより、コンテナのプロセスに独自のネットワーク スタックが与えられます。`--publish` フラグは、コンテナを介したネットワーキングをホストに公開する機能です。

どのようにしてポート 80 が nginx の既定のポートであることを知るのでしょうか？Docker Hub の [ドキュメント](https://hub.docker.com/_/nginx) に記載されているからです。一般的に、検証済みイメージのドキュメントは非常に充実しており、それらのイメージを使用してコンテナを実行する際には参照することが望ましいです。

また、`--name` フラグを指定しています。これにより、コンテナに名前を付けることができます。すべてのコンテナには名前がありますが、指定しない場合、Docker がランダムに割り当てます。独自の名前を指定することで、コンテナの ID ではなく名前を参照することができるため、コンテナに対して後続のコマンドを実行するのが簡単になります。たとえば、`docker container inspect nginx` の代わりに `docker container inspect 5e1` を使用できます。

これが初めて nginx コンテナを実行するため、Docker Store から nginx イメージをダウンロードします。Nginx イメージから作成される後続のコンテナは、ホスト上にある既存のイメージを使用します。

Nginx は軽量なウェブ サーバーです。LabEx VM の **Web 8080** タブで nginx サーバーにアクセスできます。切り替えてページを更新すると、nginx の出力が表示されます。

![step 2 nginx](../assets/20230829-11-16-04-BazUogDa.png)

## `mongo` DB サーバーを実行する

次に、mongoDB サーバーを実行します。Docker Hub からの [公式 mongoDB イメージ](https://hub.docker.com/_/mongo) を使用します。`latest` タグ（指定しない場合の既定値）ではなく、mongo イメージの特定のバージョン：4.4 を使用します。

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

同様に、これが初めて mongo コンテナを実行するため、Docker Store から mongo イメージをダウンロードします。`--publish` フラグを使用して、ホスト上の 27017 mongo ポートを公開します。ホスト マッピングに 8080 以外のポートを使用する必要があります。なぜなら、そのポートは既にホスト上で公開されているからです。再度、Docker Hub の [公式ドキュメント](https://hub.docker.com/_/mongo) を参照して、mongo イメージの使用に関する詳細を取得してください。

Web ブラウザで `0.0.0.0:8081` を使用して mongoDB の出力を確認します。MongoDB からの警告メッセージが返されるはずです。

![MongoDB server output warning](../assets/20230829-11-19-23-PkodKK48.png)

`docker container ls` で実行中のコンテナを確認します。

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." Less than a second ago Up 2 seconds 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 17 seconds ago Up 19 seconds 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 5 minutes ago Up 5 minutes priceless_kepler
```

ホスト上に Nginx ウェブ サーバー コンテナと MongoDB コンテナが実行されていることがわかります。これらのコンテナが互いに通信するように構成されていないことに注意してください。

コンテナに与えた「nginx」と「mongo」の名前と、ubuntu コンテナに生成されたランダムな名前（私の場合は「priceless_kepler」）が表示されます。また、`--publish` フラグで指定したポート マッピングも確認できます。これらの実行中のコンテナの詳細情報を取得するには、`docker container inspect [コンテナ ID]` コマンドを使用できます。

おそらく気付いたことですが、mongo コンテナは `docker-entrypoint` コマンドを実行しています。これは、コンテナが起動する際に実行される実行可能ファイルの名前です。mongo イメージは、DB プロセスを開始する前にいくつかの事前設定が必要です。[github](https://github.com/docker-library/mongo) で確認することで、このスクリプトが何を行うかを正確に把握できます。通常、Docker Store ウェブサイトのイメージ説明ページから github ソースへのリンクを見つけることができます。

コンテナは独立しており、孤立しているため、異なるシステムまたはランタイムの依存関係を持つコンテナ間の潜在的な競合を回避できます。たとえば、Java 7 を使用するアプリケーションと Java 8 を使用する別のアプリケーションを同じホストに展開する場合。または、すべてが既定のリッスン ポートとしてポート 80 を持つ複数の nginx コンテナを実行する場合（`--publish` フラグを使用してホストに公開する場合、ホストに選択されるポートは一意である必要があります）。Linux ネームスペースのおかげで、孤立の利点が得られます。

**注**: これらのプロセスを実行するために、ホストに何かをインストールする必要はありません（Docker 以外）！各コンテナには、コンテナ内で必要な依存関係が含まれているため、ホストに直接何かをインストールする必要はありません。

同じホスト上で複数のコンテナを実行することで、単一のホスト上で利用可能なリソース（CPU、メモリなど）を最大限に活用できます。これにより、企業にとって大幅なコスト削減が可能になります。

Docker Hub から直接イメージを実行することは時々便利ですが、カスタム イメージを作成し、公式イメージをこれらのイメージの起点として参照する方がもっと便利です。実験 2 で独自のカスタム イメージを構築する方法について詳しく見ていきましょう。
