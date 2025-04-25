# 合并分支并创建合并提交

作为一名开发者，你可能需要将一个分支合并到当前分支，并创建一个合并提交。如果你不熟悉 Git，这可能会有点棘手。问题是要使用名为 `https://github.com/labex-labs/git-playground` 目录的 Git 仓库，将一个分支合并到当前分支，并创建一个合并提交。

## 任务

对于这个挑战，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 克隆仓库，导航到该目录并配置身份。
2. 创建并切换到一个名为 `feature-branch` 的分支。
3. 将“这是新的一行。”添加到 `README.md` 文件中，将其添加到暂存区并提交，提交消息为“向 README.md 添加新行”。
4. 切换到 `master` 分支。
5. 将 `feature-branch` 合并到 `master` 分支，这将创建一个消息为“合并 feature-branch”的合并提交。

这是运行 `git log` 的结果：

```shell
ADD new line to README.md
```
