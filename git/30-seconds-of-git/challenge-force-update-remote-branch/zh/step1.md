# 改写历史记录后更新远程分支

当你在本地改写历史记录时，你会创建一个具有不同 SHA-1 哈希值的新提交。这意味着你本地分支上的提交历史与远程分支上的提交历史不同。如果你尝试将更改推送到远程分支，Git 会拒绝推送，因为它会认为提交历史已经分叉。要解决这个问题，你需要强制更新远程分支。

## 任务

要完成这个挑战，你将使用你 GitHub 账户中的 `git-playground` Git 仓库，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。

1. 将 `git-playground` 仓库克隆到你的本地机器。
2. 将提交消息为「Added file2.txt」的提交更新为提交消息为「Update file2.txt」的提交。
3. 将本地分支的更改推送到远程仓库。
4. 如果你无法成功推送，请强制推送。

这是最终结果：

```shell
[object Object]
```
