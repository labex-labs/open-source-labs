# 別のブランチにリベースする

開発者として、複数のブランチがあるプロジェクトを担当しています。自分のブランチに変更を加え、それらの変更を別のブランチに取り込みたいと思っています。ただし、クリーンで線形の履歴を維持したいため、ブランチをマージしたくありません。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. ディレクトリに移動し、識別情報を設定します。
2. `one-branch` という名前のブランチを作成し、切り替えます。
3. `README.md` ファイルに "hello,world" を追加し、ステージング エリアに追加して、メッセージ "Added some changes to README.md" でコミットします。
4. `master` ブランチに切り替えます。
5. ローカルの `master` ブランチがリモート リポジトリと最新であることを確認します。
6. `one-branch` を `master` ブランチにリベースします。
7. リベース プロセス中に発生するすべてのコンフリクトを解消します。

これが `git log` を実行した結果です。

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
