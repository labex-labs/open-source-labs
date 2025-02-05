# 在特定日期范围内查看提交记录

你的任务是使用Git查看特定日期范围内的所有提交记录。你需要使用带有 `--since` 和 `--until` 选项的 `git log` 命令来指定日期范围。你可以使用具体日期或相对日期（例如 “12周前”）。

要完成此挑战，你需要使用 `https://github.com/labex-labs/git-playground` 仓库。请按照以下步骤操作：

1. 使用命令 `git clone https://github.com/labex-labs/git-playground` 将仓库克隆到你的本地机器。
2. 使用命令 `cd git-playground` 导航到仓库目录。
3. 使用命令 `git log --since='Apr 25 2023' --until='Apr 27 2023'` 查看2023年4月25日至2023年4月27日之间的所有提交记录。
4. 使用命令 `git log --since='12 weeks ago'` 查看过去十二周内的所有提交记录。

这是最终结果：

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
