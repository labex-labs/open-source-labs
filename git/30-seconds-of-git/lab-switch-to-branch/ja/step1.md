# ブランチに切り替える

あなたは `https://github.com/labex-labs/git-playground` という名前の Git リポジトリ内のプロジェクトを作業してきました。あなたのチームは、新しい機能を開発するために `feature-1` という名前の新しいブランチを作成しました。あなたはこの機能の作業を続けるために `feature-1` ブランチに切り替える必要があります。

1. Git リポジトリをクローンする：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. リポジトリディレクトリに移動する：

```shell
cd git-playground
```

3. リポジトリ内のすべてのブランチを一覧表示する：

```shell
git branch
```

出力：

```shell
feature-1
* master
```

4. `feature-1` ブランチに切り替える：

```shell
git checkout feature-1
```

出力：

```shell
Switched to branch 'feature-1'
```

5. 現在 `feature-1` ブランチにいることを確認する：

```shell
git branch
```

出力：

```shell
* feature-1
master
```
