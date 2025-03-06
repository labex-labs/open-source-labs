# 特定の日付範囲内のコミットを表示する

ここでは、特定の日付に基づいてコミットをフィルタリングする方法を学びます。Git はこの目的のために 2 つの便利なオプションを提供しています。

- `--since` または `--after`：特定の日付以降のコミットを表示します。
- `--until` または `--before`：特定の日付以前のコミットを表示します。

これらのオプションを組み合わせることで、特定の日付範囲内のコミットを表示できます。

2023 年 4 月 25 日から 2023 年 4 月 27 日までに行われたすべてのコミットを表示してみましょう。

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

このコマンドは、2023 年 4 月 25 日から 4 月 27 日までに行われたすべてのコミットを表示します。出力は次のようになるはずです。

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

Git は多くの日付形式を受け付けます。以下がその例です。

- `"YYYY-MM-DD"`（例：`2023-04-25`）
- `"Month DD YYYY"`（例：`Apr 25 2023`）
- `"DD Month YYYY"`（例：`25 Apr 2023`）

別の日付形式を試して、異なる範囲内にコミットがあるかどうかを確認してみましょう。

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

この期間中にコミットがなかった場合、このコマンドは結果を返さないことがありますが、これは正常な現象です。
