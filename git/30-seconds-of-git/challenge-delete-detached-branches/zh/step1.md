# 删除分离头指针分支

你有一个 Git 仓库，其中包含几个你不再需要的分离头指针分支。这些分支使你的仓库变得杂乱，难以管理。你想要删除所有分离头指针分支以清理你的仓库。

## 任务

要完成此挑战，你将使用来自你 GitHub 账户的 Git 仓库 `git-playground`，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。不要勾选「仅复制主分支」。

1. 克隆仓库，导航到该目录并配置身份。
2. 由于远程仓库中有一个 `feature-branch` 分支，切换到 `feature-branch`，这将使本地的 `feature-branch` 跟踪远程仓库的 `feature-branch` 分支，并删除远程仓库中的 `feature-branch` 分支。
3. 查看本地分支与其跟踪的远程分支之间的跟踪关系。
4. 切换回 `master` 分支。
5. 从你的本地仓库中删除所有分离头指针分支。
6. 验证分离头指针分支是否已被删除。

输出应仅显示与特定分支相关联的分支：

```shell
* master d22f46b [origin/master] Added file2.txt
```
