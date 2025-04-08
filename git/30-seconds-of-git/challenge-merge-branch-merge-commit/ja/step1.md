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



ADD new line to README.md
```
