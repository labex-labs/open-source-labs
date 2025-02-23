# コミットを新しいブランチに移動させる

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。あなたは `master` ブランチでプロジェクトを作業してきました。あなたは、あなたが行った変更の一部が別のブランチで行われるべきだったことに気付きます。これらの変更を `feature` と呼ばれる新しいブランチに移動させたいと思います。

## タスク

1. リポジトリディレクトリに移動し、GitHub の ID を設定します。
2. `master` ブランチをチェックアウトします。
3. `hello.txt` という名前のファイルを作成し、そこに "hello, world" を追加し、ステージングエリアに追加して、メッセージ "Added hello.txt" でコミットします。
4. 新しいブランチ `feature` を作成して、切り替えません。
5. `master` の最後のコミットを元に戻します。
6. `master` ブランチのコミット履歴と `feature` ブランチのコミット履歴を確認して、結果を確認します。

これは `git log` を実行した結果です。

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
