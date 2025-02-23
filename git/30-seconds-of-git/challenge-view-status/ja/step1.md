# 現在の状態を表示する

開発者として、Git リポジトリの現在の状態を把握することは重要です。これには、どのファイルが変更されたか、コミットのためにステージングされたファイル、および追跡されていないファイルに関する情報が含まれます。

あなたのタスクは、`https://github.com/labex-labs/git-playground` にある Git リポジトリの現在の状態を表示することです。コマンドの出力に注意を払い、その意味を理解しようとしてください。

## タスク

このチャレンジを完了するには、`https://github.com/labex-labs/git-playground` にある Git リポジトリをクローンする必要があります。

1. リポジトリをクローンしたら、リポジトリのルート ディレクトリに移動します。
2. Git リポジトリの現在の状態を表示します。

これにより、ワーキング ツリーの現在の状態が出力されます。現在どのブランチにいるか、ローカル ブランチがリモート リポジトリと最新かどうか、および追跡されていないファイルや変更されたファイルに関する情報が表示されるはずです。

出力は次のようになります。

```shell
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
