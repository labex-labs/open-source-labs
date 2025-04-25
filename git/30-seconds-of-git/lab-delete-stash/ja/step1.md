# Git のスタッシュを削除する

`https://github.com/labex-labs/git-playground` という名前の Git リポジトリがあります。 `git stash save "my stash"` コマンドを使用してスタッシュを作成しました。これ以上必要がないので、このスタッシュを削除したいと思います。

1. `cd git-playground` コマンドを使用してリポジトリディレクトリに移動します。
2. `git stash list` コマンドを使用してすべてのスタッシュを一覧表示します。先ほど作成したスタッシュが表示されるはずです。
3. `git stash drop stash@{0}` コマンドを使用してスタッシュを削除します。
4. `git stash list` コマンドを再度使用してすべてのスタッシュを一覧表示します。

先ほど削除したスタッシュはもはや表示されないはずです。
