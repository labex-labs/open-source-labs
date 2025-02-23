# 最新のスタッシュを適用する

あなたは Git リポジトリ内のプロジェクトを作業しており、コミットする準備ができていないいくつかの変更を加えました。しかし、別の機能を開発するために、別のブランチに切り替えたり、コミットする必要があります。変更を失いたくないので、スタッシュに保存することにします。後で、変更を続ける準備ができたら、最新のスタッシュを作業ディレクトリに適用する必要があります。

Git リポジトリに最新のスタッシュを適用するには、次の手順に従います。

1. `https://github.com/labex-labs/git-playground` という名前の Git リポジトリをローカルマシンにクローンします。
2. `git-playground` ディレクトリに移動します。
3. `README.md` ファイルにいくつかの変更を加えます。たとえば、`README.md` ファイルに "This is a new line" と書き込みます。
4. コマンド `git stash` を実行して変更をスタッシュに保存します。
5. コマンド `git stash list` を実行して、スタッシュの一覧を表示します。一覧に 1 つのスタッシュが表示されるはずです。
6. コマンド `git stash apply` を実行して、最新のスタッシュを作業ディレクトリに適用します。
7. `README.md` ファイルを確認して、変更が適用されていることを確認します。

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

これが `cat README.md` を実行した結果です。

```shell
# git-playground
Git Playground
This is a new line
```
