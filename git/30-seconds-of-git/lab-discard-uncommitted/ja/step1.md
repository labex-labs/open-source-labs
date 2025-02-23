# 未コミットの変更を破棄する

ローカルの Git リポジトリにいくつかの変更を加えましたが、まだコミットしていません。 しかし、これらの変更を保持したくなくなり、破棄したいと判断しました。 問題は、現在のブランチに対するすべての未コミットの変更を破棄する方法を見つけることです。

このチャレンジを完了するには、`https://github.com/labex-labs/git-playground` ディレクトリの Git リポジトリを使用します。 以下の手順に従ってください。

1. `git clone https://github.com/labex-labs/git-playground.git` コマンドを使用して、リポジトリをローカルマシンにクローンします。
2. `cd git-playground` コマンドを使用して、クローンしたリポジトリに移動します。
3. `echo "hello,world" > hello.txt` および `git add.` コマンドを使用して、リポジトリ内のファイルにいくつかの変更を加えますが、コミットしません。
4. `git status` コマンドを使用して、加えた変更を確認します。
5. `git reset --hard HEAD` コマンドを使用して、すべての未コミットの変更を破棄します。
6. すべての変更が破棄されたことを確認するために、再度 `git status` コマンドを使用します。

これが `git status` を実行した結果です。

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
