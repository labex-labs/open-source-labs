# 变基到另一个分支

作为一名开发者，你正在处理一个有多个分支的项目。你已经在自己的分支上做了一些更改，并希望将这些更改合并到另一个分支中。然而，你不想直接合并分支，因为你希望保持提交历史的简洁和线性。

## 任务

在本次挑战中，我们将使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 进入该仓库目录并配置身份信息。
2. 创建并切换到一个名为 `one-branch` 的分支。
3. 在 `README.md` 文件中添加 "hello,world"，将其添加到暂存区，并提交，提交信息为 "Added some changes to README.md"。
4. 切换到 `master` 分支。
5. 确保你的本地 `master` 分支与远程仓库保持同步。
6. 将 `one-branch` 分支变基到 `master` 分支上。
7. 解决变基过程中出现的任何冲突。

这是运行 `git log` 的结果：

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
