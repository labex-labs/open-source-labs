# Git Cherry-Pick

開発者として、複数のブランチがあるプロジェクトを担当しています。以前のコミットで行われた特定の変更を、現在のブランチに適用したいと思っています。ただし、そのブランチには必要ない他の変更も含まれているため、エンタイアなブランチをマージしたくありません。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. ディレクトリに移動して ID を設定します。
2. `one-branch` という名前のブランチを作成して切り替え、`hello.txt` という名前のファイルを作成し、その中に "hello,world" を書き込み、ステージングエリアに追加して、メッセージ "add hello.txt" でコミットします。
3. 前の手順で作成したコミットのハッシュを特定して、`master` ブランチに適用します。
4. `master` ブランチをチェックアウトして、`master` ブランチに変更を適用します。
5. `master` ブランチに変更が適用されたことを確認します。

これが `master` ブランチで `git log` を実行した結果です：

```shell
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
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
