# ブランチをマージしてマージコミットを作成する

開発者として、ブランチを現在のブランチにマージしてマージコミットを作成する必要がある場合があります。Git に慣れていない場合は、これが少し厄介になることがあります。問題は、`https://github.com/labex-labs/git-playground` ディレクトリの Git リポジトリを使用して、ブランチを現在のブランチにマージしてマージコミットを作成することです。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
2. `feature-branch` と呼ばれるブランチを作成して切り替えます。
3. `README.md` ファイルに "This is a new line." を追加し、ステージング エリアに追加してコミットします。コミット メッセージは "Add new line to README.md" です。
4. `master` ブランチに切り替えます。
5. `feature-branch` を `master` ブランチにマージします。これにより、メッセージ "Merge feature-branch" のマージコミットが作成されます。

これが `git log` を実行した結果です。

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
