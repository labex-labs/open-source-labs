# ブランチをマージしてマージコミットを作成する

開発者として、ブランチを現在のブランチにマージしてマージコミットを作成する必要がある場合があります。Git に慣れていない場合は、これが少し難しい場合があります。問題は、`https://github.com/labex-labs/git-playground` ディレクトリの Git リポジトリを使用して、ブランチを現在のブランチにマージしてマージコミットを作成することです。

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. `https://github.com/labex-labs/git-playground.git` からリポジトリをクローンする：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. ディレクトリに移動して ID を設定する：

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `feature-branch` と呼ばれるブランチを作成して切り替える：

```shell
git checkout -b feature-branch
```

4. `README.md` ファイルに "This is a new line." を追加し、ステージングエリアに追加してコミットし、コミットメッセージは "Add new line to README.md" とする：

```shell
echo "This is a new line." >> README.md
git add.
git commit -am "Add new line to README.md"
```

5. `master` ブランチに切り替える：

```shell
git checkout master
```

6. `feature-branch` を `master` ブランチにマージして、メッセージ "Merge feature-branch" のマージコミットを作成する：

```shell
git merge --no-ff -m "Merge feature-branch" feature-branch
```

これが `git log` を実行した結果です：

```shell
commit 45b7e0fa8656d0aa751c7ca3cee29422e3d6cf05 (HEAD -> master)
Merge: d22f46b 1f19499
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Merge feature-branch

commit 1f1949955387a154ff1bb5286d3d0a2b993f87e0 (feature-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add new line to README.md
```
