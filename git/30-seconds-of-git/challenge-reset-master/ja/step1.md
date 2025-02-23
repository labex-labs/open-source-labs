# ローカルの master ブランチをリモートに合わせる

あなたはプロジェクトに取り組んでおり、ローカルの `master` ブランチに変更を加えてきました。しかし、ローカルブランチにはない新しい変更がリモートの `master` ブランチに更新されていることに気づきました。あなたは、ローカルの `master` ブランチをリモートのブランチに合わせるためにリセットする必要があります。

## タスク

1. `master` ブランチに切り替えます。
2. リモートから最新の更新を取得します。
3. 現在のブランチのコミット履歴を表示します。
4. ローカルの `master` ブランチをリモートのブランチに合わせるためにリセットします。
5. ローカルの `master` ブランチが現在リモートの `master` ブランチと最新であることを確認します。

これが完成した結果です：

```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
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
