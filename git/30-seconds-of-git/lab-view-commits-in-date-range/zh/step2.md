# 探索基本的 `git log` 命令

现在我们已经克隆了仓库，让我们来学习如何使用 `git log` 命令查看提交历史。

`git log` 命令会显示仓库中所有提交的列表，从最近的提交开始。每个提交记录包含以下信息：

- 唯一的提交哈希值（标识符）
- 作者信息
- 提交的日期和时间
- 提交信息

让我们查看基本的提交历史：

```bash
git log
```

你应该会看到类似以下的输出：

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

如果输出内容很长，你可以使用以下操作进行浏览：

- 按 `Space` 键向前翻页
- 按 `b` 键向后翻页
- 按 `q` 键退出日志视图

请注意，每个提交都有一个唯一的标识符（长十六进制字符串）、作者信息、提交的日期和时间，以及描述所做更改的信息。
