# 从远程获取最新变更

假设你正在与一组开发人员合作一个项目，该项目存储在远程仓库中。你希望从远程仓库获取最新变更，但不将其应用到本地仓库。

## 任务

为了演示如何从远程仓库获取最新变更，我们将使用你 GitHub 账户中的 `git-playground` 仓库，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。

1. 克隆仓库，导航到该目录。
2. 在 Github 网站上你的账户中找到 `git-playground` 仓库，创建并切换到一个名为 `fetch-branch` 的分支，创建一个名为 `hello.txt` 的文件，添加“hello, world”并提交，提交消息为“Create hello.txt”。
3. 查看远程仓库中的分支。
4. 从远程仓库获取最新变更。
5. 再次查看远程仓库中的分支，并验证是否已获取到最新变更。

这是运行 `git log origin/fetch-branch` 的结果：

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
