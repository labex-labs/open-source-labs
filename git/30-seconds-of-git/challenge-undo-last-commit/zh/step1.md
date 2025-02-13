# 撤销最后一次提交

你刚刚将更改提交到了你的 Git 仓库，但你意识到自己犯了一个错误。你想撤销最后一次提交，同时又不丢失你所做的任何更改。你该怎么做呢？

## 任务

对于这个挑战，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 查看提交历史记录。
2. 撤销最后一次提交，使用该提交更改的反向操作创建一个新的提交。

这是运行 `git log --oneline` 命令的结果：

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
