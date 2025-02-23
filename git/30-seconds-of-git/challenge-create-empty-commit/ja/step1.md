# 空のコミットを作成する

Git リポジトリに空のコミットを作成する必要があります。これは、次のようないくつかのシナリオで役立ちます。

- ビルドプロセスをトリガーする
- プレースホルダーとしてのコミットを作成する
- リポジトリの履歴における特定のポイントをマークする

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. リポジトリディレクトリに移動し、環境に GitHub の ID を設定します。
2. メッセージ "Empty commit" で空のコミットを作成します。
3. 空のコミットが作成されたことを確認します。

ここで `git log --name-status HEAD^..HEAD` を実行した結果です。

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
