# 将提交移动到新分支

对于这个挑战，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。你一直在 `master` 分支上处理一个项目。你意识到你所做的一些更改本应在一个单独的分支上进行。你想将这些更改移动到一个名为 `feature` 的新分支上。

## 任务

1. 导航到仓库目录并配置你的 GitHub 身份。
2. 检出 `master` 分支。
3. 创建一个名为 `hello.txt` 的文件，在其中添加 "hello, world"，将其添加到暂存区并提交，提交消息为 "Added hello.txt"。
4. 创建一个名为 `feature` 的新分支，但不切换到它。
5. 撤销 `master` 分支上的最后一次提交。
6. 检查 `master` 分支上的提交历史记录和 `feature` 分支上的提交历史记录，以验证结果。

这是运行 `git log` 的结果：

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```
