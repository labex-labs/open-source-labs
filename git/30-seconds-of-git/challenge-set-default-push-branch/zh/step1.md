# 设置默认推送分支名称

当将更改推送到远程仓库时，Git 会使用当前本地分支的名称作为远程分支的默认名称。然而，有时你可能希望将更改推送到不同的分支。在这种情况下，每次推送更改时都需要显式指定远程分支的名称。这可能会很繁琐且容易出错，尤其是当你使用多个分支时。

## 任务

要完成此挑战，你将使用 GitHub 账户中的 Git 仓库 `git-playground`，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。按照以下步骤设置默认推送分支名称：

1. 从 `https://github.com/your-username/git-playground.git` 克隆仓库。
2. 切换到仓库目录。
3. 将默认推送分支名称设置为当前本地分支的名称。
4. 创建一个名为 `my-branch` 的新分支并切换到该分支。
5. 创建一个名为 `hello.txt` 的新文件，并在其中写入字符串 "Hello, World"。将新创建的文件 `hello.txt` 添加到 Git 暂存区并提交，使用提交消息 "Add hello.txt" 来描述此提交中所做的更改。
6. 将你的更改推送到远程仓库。Git 将把你的更改推送到远程仓库上名为 `my-branch` 的分支。

这是运行 `git log` 的结果：

```shell

ADD hello.txt
```
