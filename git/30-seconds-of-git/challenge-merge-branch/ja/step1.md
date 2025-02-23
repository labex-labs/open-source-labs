# ブランチをマージする

あなたのタスクは、Git を使ってブランチを現在のブランチにマージすることです。ターゲット ブランチに切り替え、その後ソース ブランチをマージする必要があります。これは、`feature-branch-A` ブランチの変更をプロジェクトの `master` ブランチに結合したい場合に便利です。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. ディレクトリに移動し、識別情報を設定します。
2. `feature-branch-A` ブランチを作成します。そのブランチに切り替えます。
3. `file2.txt` ファイルに "hello,world" を追加し、ステージング エリアに追加し、メッセージ "fix file2.txt" でコミットします。
4. `master` ブランチに切り替えます。
5. `feature-branch-A` を `master` ブランチにマージします。
6. マージ プロセス中に発生する可能性のあるコンフリクトを解消します。

これが `git log` を実行した結果です。

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
