# 查看特定日期范围内的提交

现在我们将学习如何根据特定日期过滤提交。Git 为此提供了两个有用的选项：

- `--since` 或 `--after`：显示比特定日期更新的提交
- `--until` 或 `--before`：显示比特定日期更旧的提交

当我们组合使用这些选项时，就可以查看特定日期范围内的提交。

让我们查看 2023 年 4 月 25 日至 2023 年 4 月 27 日之间发生的所有提交：

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

此命令将显示 2023 年 4 月 25 日至 4 月 27 日之间所做的所有提交。输出应该如下所示：

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

Git 接受多种日期格式，包括：

- `"YYYY-MM-DD"`（例如，`2023-04-25`）
- `"Month DD YYYY"`（例如，`Apr 25 2023`）
- `"DD Month YYYY"`（例如，`25 Apr 2023`）

尝试使用另一种日期格式，看看不同日期范围内是否有提交：

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

如果在该时间段内没有提交，此命令可能不会返回任何结果，这是完全正常的。
