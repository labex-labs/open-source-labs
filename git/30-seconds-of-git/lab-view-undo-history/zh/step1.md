# 查看 “撤销” 历史记录

作为一名开发者，你可能需要撤销对代码库所做的更改。Git 提供了几种撤销更改的方法，比如使用 `git reset` 或 `git revert` 命令。然而，要跟踪你所执行的所有操作可能会很困难，尤其是当你使用了像 `git rebase` 这样更高级的命令时。这就是 `git reflog` 命令派上用场的地方。

`git reflog` 命令会显示 Git 引用日志，它记录了你在仓库中执行的所有操作。这不仅包括提交，还包括其他操作，如分支合并、变基和重置。通过查看引用日志，你可以看到对仓库所做的所有更改的完整历史记录，即使它们没有显示在提交历史中。

要查看 Git 中的 “撤销” 历史记录，你可以使用 `git reflog` 命令。假设你对一个仓库做了一些更改，然后想要撤销它们。

1. 使用命令行导航到仓库：

```shell
cd git-playground
```

2. 现在，假设你意识到自己犯了一个错误，想要撤销上一次提交。你可以使用 `git reset` 命令来做到这一点：

```shell
git reset HEAD~1
```

3. 运行此命令后，你可能会意识到自己又犯了另一个错误，想要撤销这次重置。这就是 `git reflog` 命令派上用场的地方。你可以使用它来查看引用日志，并找到上一次提交的提交哈希：

```shell
git reflog
```

这将显示你在仓库中执行的所有操作的列表，包括这次重置：

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```

4. 从这个输出中，你可以看到上一次提交的哈希是 `d22f46b`。你可以使用这个哈希将仓库重置回上一次提交：

```shell
git reset d22f46b
```

5. 查看历史提交记录以验证结果：

```shell
git log
```
