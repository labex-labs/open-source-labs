# 現在の状態を表示する

開発者として、Git リポジトリの現在の状態を知ることは重要です。これには、どのファイルが変更されたか、コミットのためにステージングされているファイル、および追跡されていないファイルに関する情報が含まれます。`git status` コマンドは、この情報を読みやすい形式で提供します。

あなたのタスクは、`https://github.com/labex-labs/git-playground` にある Git リポジトリの現在の状態を表示するために `git status` コマンドを使用することです。コマンドの出力に注意し、その意味を理解しようとしてください。

この実験を完了するには、`https://github.com/labex-labs/git-playground` にある Git リポジトリをクローンする必要があります。

1. リポジトリをクローンしたら、リポジトリのルートディレクトリに移動します。

```shell
cd git-playground
```

2. Git リポジトリの現在の状態を表示します。

```shell
git status
```

これにより、ワーキングツリーの現在の状態が出力されます。現在どのブランチにいるか、ローカルブランチがリモートリポジトリと最新かどうか、および追跡されていないファイルや変更されたファイルに関する情報が表示されます。

出力は次のようになります。

```shell
[object Object]
```
