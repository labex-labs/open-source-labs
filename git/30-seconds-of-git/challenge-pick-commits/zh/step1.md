# Git 挑选提交

作为一名开发者，你正在处理一个有多个分支的项目。你已经确定了之前一次提交中所做的特定更改，并且希望将其应用到当前分支。然而，你不想合并整个分支，因为它包含了你不需要的其他更改。

## 任务

对于这个挑战，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到该目录并配置身份信息。
2. 创建并切换到一个名为 `one-branch` 的分支，创建一个名为 `hello.txt` 的文件，在其中写入 "hello,world"，将其添加到暂存区，并使用消息 "add hello.txt" 提交它。
3. 确定上一步中创建的提交的哈希值，以便应用到 `master` 分支。
4. 检出 `master` 分支，并将更改应用到 `master` 分支。
5. 验证更改是否已应用到 `master` 分支。

这是在 `master` 分支上运行 `git log` 的结果：

```shell

ADD hello.txt
```
