# 禁用快进合并

默认情况下，Git 使用快进合并来合并没有分歧提交的分支。这意味着如果你有一个没有新提交的分支，Git 会简单地将你正在合并到的分支的指针移动到你正在合并自的分支的最新提交。虽然这在某些情况下可能有用，但它也可能导致问题，特别是在处理有多个贡献者的大型项目时。例如，如果两个开发者在同一个分支上工作并且都进行了更改，快进合并可能会导致难以解决的冲突。

## 任务

要禁用快进合并，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到该目录并配置身份。
2. 创建并切换到一个名为 `my-branch` 的分支，创建一个 `hello.txt` 文件并在其中添加 "hello,world"，将其添加到暂存区并使用消息 "Added hello.txt" 提交。
3. 为所有分支禁用快进合并。
4. 切换回 `master` 分支并合并 `my-branch` 分支，保存并退出而不更改文本。

现在，即使可以快进，Git 也将始终创建一个合并提交：

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
