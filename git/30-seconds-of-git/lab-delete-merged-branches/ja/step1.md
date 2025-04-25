# マージ済みブランチの削除

あなたのタスクは、`https://github.com/labex-labs/git-playground` リポジトリの `master` ブランチにマージされたすべてのローカルブランチを削除することです。

1. リポジトリディレクトリに移動します。

```shell
cd git-playground
```

2. `master` にマージされたすべてのローカルブランチを一覧表示します。

```shell
git branch --merged
```

出力：

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3. すべてのマージ済みブランチを削除します。

```shell
git branch --merged master | awk '!/^[ *]*$/ &&!/master/ {print $1}' | xargs git branch -d
```

4. 再度すべてのブランチを一覧表示します。

```shell
git branch
```

これが最終結果です。

```
* master
```
