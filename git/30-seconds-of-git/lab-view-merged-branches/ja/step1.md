# マージ済みのブランチを表示する

あなたのタスクは、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリ内のすべてのマージ済みのローカルブランチの一覧を表示することです。マージ済みのブランチの一覧を表示するには、`git branch -a --merged` コマンドを使用します。一覧を取得したら、矢印キーを使ってそれを参照し、<kbd>Q</kbd> キーを押すことで終了できるようにしてください。

1. リポジトリディレクトリに移動する：

```shell
cd git-playground
```

2. マージ済みのブランチの一覧を表示する：

```shell
git branch -a --merged
```

これが最終結果です：

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
