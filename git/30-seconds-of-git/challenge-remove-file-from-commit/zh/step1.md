# 从最后一次提交中移除文件

你不小心将一个本不打算包含的文件添加到了最后一次提交中。你希望在不更改提交消息的情况下，将该文件从最后一次提交中移除。

## 任务

对于本次挑战，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。假设你有一个名为 `git-playground` 的 Git 仓库，其中有一个名为 `file2.txt` 的文件，你不小心将其添加到了最后一次提交中。

1. 导航到仓库目录并配置你的 GitHub 身份。
2. 从暂存区移除指定的 `file2.txt`。
3. 更新最后一次提交的内容，同时不更改其提交消息。

运行这些命令后，`file2.txt` 文件将从最后一次提交中移除，且不更改其提交消息。

这是当你从 Git 版本控制系统中移除 `file2.txt` 时发生的情况：

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
