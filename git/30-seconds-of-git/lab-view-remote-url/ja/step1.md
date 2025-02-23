# リモート URL を表示する

開発者として、Git の設定のトラブルシューティングや正しいリポジトリで作業していることを確認するなど、さまざまな理由でリモート リポジトリの URL を表示する必要がある場合があります。ただし、Git コマンドに慣れていない場合は、リモート URL をどのように表示するかを知るのが難しい場合があります。

この実験では、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリを使用します。このリポジトリのリモート URL を表示するには、次の手順に従います。

1. ターミナルまたはコマンド プロンプトを開きます。
2. `git-playground` リポジトリをクローンしたディレクトリに移動します。

```shell
cd git-playground
```

3. 次のコマンドを実行して、リモート URL を表示します。

```shell
git config --get remote.origin.url
```

出力には、この場合 `https://github.com/labex-labs/git-playground.git` であるリモート リポジトリの URL が表示されます。
