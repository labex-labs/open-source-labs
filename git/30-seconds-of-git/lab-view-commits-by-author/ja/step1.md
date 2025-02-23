# 作者によるコミットの表示

あなたのタスクは、`git-playground` リポジトリで特定の作者によって作成されたすべてのコミットを取得することです。このリポジトリには、Git のスキルを練習するために使用できるサンプル プロジェクトのコレクションが含まれています。

この実験を完了するには、`--author` オプション付きで `git log` コマンドを使用する必要があります。これにより、コミット履歴をフィルタリングして、指定された作者によって作成されたコミットのみを表示できます。

`git-playground` リポジトリで作者「Hang」によって作成されたすべてのコミットを取得するには、次のコマンドを使用できます。

```shell
git log --author="Hang"
```

これにより、リポジトリで「Hang」によって作成されたすべてのコミットのリストと、コミット メッセージ、日付、その他の詳細に関する情報が出力されます。

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/
master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
