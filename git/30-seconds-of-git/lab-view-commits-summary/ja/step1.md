# コミットの短い要約を表示する

開発者として、複数の貢献者が参加するプロジェクトを担当しています。プロジェクトに対して行われたすべてのコミットの要約を表示して、行われた変更を理解し、潜在的な問題を特定する必要があります。ただし、必要な情報を見つけるためにすべてのコミットメッセージを精査するのに多くの時間を費やしたくありません。

Git リポジトリに対して行われたすべてのコミットの短い要約を表示するには、`git log --oneline` コマンドを使用できます。たとえば、GitHub 上にホストされている `git-playground` という名前のプロジェクトを担当しているとしましょう。

1. 次のコマンドを使用して、リポジトリをローカル マシンにクローンできます。

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. リポジトリをクローンしたら、プロジェクト ディレクトリに移動し、次のコマンドを実行して、すべてのコミットの短い要約を表示します。

```shell
cd git-playground
git log --oneline
```

これにより、リポジトリに対して行われたすべてのコミットの一覧と、各コミット メッセージの短い要約が出力されます。たとえば：

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
