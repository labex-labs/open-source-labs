# 从最后一次提交中移除文件

你不小心将一个本不打算包含的文件添加到了最后一次提交中。你希望在不更改提交消息的情况下，将该文件从最后一次提交中移除。

在本次实验中，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。假设你有一个名为 `git-playground` 的 Git 仓库，其中有一个名为 `file2.txt` 的文件，你不小心将其添加到了最后一次提交中。以下是将该文件从最后一次提交中移除的步骤：

1. 克隆仓库，进入该目录并配置身份信息：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 使用 `git rm --cached <文件>` 从暂存区移除指定的 `<文件>`：

```shell
git rm --cached file2.txt
```

3. 使用 `git commit --amend` 更新最后一次提交的内容，同时不更改其提交消息：

```shell
git commit --amend --allow-empty
```

如果删除文件后提交变为空提交，则使用 `--allow-empty`，否则可以省略。

运行这些命令后，文件 `file2.txt` 将从最后一次提交中移除，且提交消息不会改变。

这是当你从 Git 版本控制系统中移除 `file2.txt` 时发生的情况：

```shell
位于主分支

待提交的变更：
(使用 "git restore --staged <文件>..." 取消暂存)
删除：file2.txt

未跟踪的文件：
(使用 "git add <文件>..." 将其包含在将提交的内容中)
file2.txt
```
