# 查看「撤销」历史记录

作为一名开发者，你可能需要撤销对代码库所做的更改。Git 提供了多种撤销更改的方法，比如使用 `git reset` 或 `git revert` 命令。然而，要跟踪你所执行的所有操作可能会很困难，尤其是当你使用了像 `git rebase` 这样更高级的命令时。

## 任务

假设你对一个仓库做了一些更改，现在想要撤销它们。

1. 进入该仓库。
2. 这时，你意识到自己犯了个错误，想要撤销上一次提交。
3. 你可能又发现自己犯了另一个错误，想要撤销刚才的重置操作。查看引用日志并找到上一次提交的提交哈希值。
4. 你发现上一次提交的哈希值是 `d22f46b`，并使用这个哈希值将仓库重置回上一次提交。
5. 查看历史提交记录以验证结果。

以下是步骤 3 的结果。这将显示你在该仓库中执行的所有操作列表，包括重置操作：

```shell
cf80005 (HEAD -> master) HEAD@{0}: reset: moving to HEAD~1
d22f46b (origin/master, origin/feature-branch, origin/HEAD) HEAD@{1}: clone: from https://github.com/labex-labs/git-playground.git
```
