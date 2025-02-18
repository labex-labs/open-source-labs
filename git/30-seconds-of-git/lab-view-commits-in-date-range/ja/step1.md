# 特定の日付範囲内のコミットを表示する

あなたのタスクは、Git を使用して特定の日付範囲内のすべてのコミットを表示することです。日付範囲を指定するには、`--since` と `--until` オプションを使用した `git log` コマンドを使用する必要があります。特定の日付または相対日付（例: "12 weeks ago"）のどちらを使用しても構いません。

このチャレンジを完了するには、`https://github.com/labex-labs/git-playground` リポジトリを使用する必要があります。以下の手順に従ってください。

1. `git clone https://github.com/labex-labs/git-playground` コマンドを使用して、リポジトリをローカルマシンにクローンします。
2. `cd git-playground` コマンドを使用して、リポジトリのディレクトリに移動します。
3. `git log --since='Apr 25 2023' --until='Apr 27 2023'` コマンドを使用して、2023 年 4 月 25 日から 2023 年 4 月 27 日までのすべてのコミットを表示します。
4. `git log --since='12 weeks ago'` コマンドを使用して、過去 12 週間以内に行われたすべてのコミットを表示します。

これが最終的な結果です。

```
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
