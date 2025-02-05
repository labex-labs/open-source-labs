# 丢弃未提交的更改

你已经对你的本地 Git 仓库做了一些更改，但还没有提交它们。然而，你决定不再保留这些更改并想要丢弃它们。问题在于找到一种方法来丢弃当前分支上所有未提交的更改。

要完成这个挑战，你将使用位于 `https://github.com/labex-labs/git-playground` 目录下的 Git 仓库。请按照以下步骤操作：

1. 使用命令 `git clone https://github.com/labex-labs/git-playground.git` 将仓库克隆到你的本地机器。
2. 使用命令 `cd git-playground` 导航到克隆的仓库。
3. 对仓库中的文件做一些更改，但不要使用命令 `echo "hello,world" > hello.txt` 和 `git add.` 提交它们。
4. 使用命令 `git status` 查看你所做的更改。
5. 使用命令 `git reset --hard HEAD` 丢弃所有未提交的更改。
6. 再次使用命令 `git status` 确认所有更改都已被丢弃。

这是运行 `git status` 的结果：

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
