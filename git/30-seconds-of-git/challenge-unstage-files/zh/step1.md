# 从暂存区移除文件

你正在 `git-playground` 仓库中处理一个项目。你已经对文件做了一些更改并将它们添加到了暂存区。然而，你意识到自己不小心添加了一个你不想提交的文件。你需要将这个文件从暂存区移除。

## 任务

1. 查看当前工作目录状态。
2. 从暂存区移除 `newfile.txt` 文件。
3. 验证该文件已从暂存区移除。

这是最终结果：

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```
