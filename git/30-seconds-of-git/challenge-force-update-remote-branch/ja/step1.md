# 履歴を書き換えた後のリモートブランチの更新

ローカルで履歴を書き換えると、異なる SHA-1 ハッシュで新しいコミットが作成されます。これは、ローカルブランチのコミット履歴がリモートブランチのコミット履歴と異なることを意味します。変更をリモートブランチにプッシュしようとすると、Git はコミット履歴が分岐していると見なしてプッシュを拒否します。この問題を解決するには、リモートブランチの更新を強制する必要があります。

## タスク

このチャレンジを完了するには、GitHub アカウントの `git-playground` Git リポジトリを使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。

1. `git-playground` リポジトリをローカルマシンにクローンします。
2. メッセージ「Added file2.txt」のコミットを、メッセージ「Update file2.txt」のコミットに更新します。
3. ローカルブランチの変更をリモートリポジトリにプッシュします。
4. 正常にプッシュできない場合は、強制的にプッシュしてください。

これが最終結果です：

```shell
commit b8c530558ecd004156dd05ac7d22d8cf07b2c28e (HEAD -> master, origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Update file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
