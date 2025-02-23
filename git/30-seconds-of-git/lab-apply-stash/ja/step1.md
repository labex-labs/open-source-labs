# スタッシュを適用する

あなたは `git-playground` リポジトリの機能ブランチで作業しており、バグ修正に取り組むために別のブランチに切り替える必要があります。ただし、まだコミットする準備ができていない変更がいくつかあります。これらの変更を保存して別のブランチに切り替えたいと思います。バグ修正が完了したら、スタッシュを適用して機能ブランチの作業を続けたいと思います。

変更は `feature-branch` ブランチにスタッシュされており、スタッシュメッセージは "my changes" です。

1. `git-playground` ディレクトリに移動します。

```shell
cd git-playground
```

2. `master` ブランチに切り替え、バグ修正後にスタッシュします。スタッシュメッセージは "fix the bug" です。`file1.txt` ファイルの内容を "hello,world" に更新することでバグを修正します。

```shell
git checkout master
echo "hello,world" > file1.txt
git stash save "fix the bug"
```

3. `feature-branch` ブランチに切り替え、スタッシュの一覧を見て、情報が "my changes" であるスタッシュを適用します。

```shell
git checkout feature-branch
git stash apply stash@{1}
```

これが `README.md` ファイルの内容です。

```
# git-playground
Git Playground
some changes
```

スタッシュする前に行った変更が現在適用されていることがわかるはずです。
