# 重命名分支

作为一名开发者，出于各种原因，你可能需要重命名分支，比如使其更具描述性或者遵循命名规范。重命名分支可能是一项简单的任务，但需要一些 Git 命令的知识。在这个挑战中，你将学习如何使用 Git 重命名分支。

对于这个实验，我们将使用名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库。

假设你将创建一个名为 `old-branch` 的分支来处理一个新功能。完成该功能后，你意识到分支名称的描述性不够。你想将该分支重命名为 `new-branch` 以使其更有意义。要重命名分支，请执行以下步骤：

1. 打开终端并导航到本地仓库目录。
2. 使用 `git checkout -b old-branch` 命令创建一个名为 `old-branch` 的分支，并使用 `git branch -m <旧名称> <新名称>` 命令重命名该分支。在我们的示例中，命令将是 `git branch -m old-branch new-branch`。
3. 使用 `git branch` 命令验证分支是否已重命名。

输出应显示新的分支名称：

```shell
master
* new-branch
```
