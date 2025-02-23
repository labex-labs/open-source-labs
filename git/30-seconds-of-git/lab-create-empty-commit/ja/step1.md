# 空のコミットを作成する

Git リポジトリに空のコミットを作成する必要があります。これは、次のようないくつかのシナリオで役立ちます。

- ビルドプロセスをトリガーする
- プレースホルダーコミットを作成する
- リポジトリの履歴の特定のポイントをマークする

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. `git clone https://github.com/labex-labs/git-playground` コマンドを使用して、リポジトリをローカルマシンにクローンします。
2. `cd git-playground` コマンドを使用してリポジトリのディレクトリに移動し、`git config --global user.name "your-uername"` および `git config --global user.email "your-email"` コマンドを使用して環境で GitHub アカウントを設定します。
3. `git commit --allow-empty -m "Empty commit"` コマンドを使用して、メッセージ "Empty commit" で空のコミットを作成します。
4. `git log --name-status HEAD^..HEAD` コマンドを使用して、空のコミットが作成されたことを確認します。

ここで `git log --name-status HEAD^..HEAD` を実行した結果です。

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
