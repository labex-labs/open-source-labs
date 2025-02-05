# 查找丢失的文件

你一直在 `git-playground` 仓库中处理一个项目。然而，你注意到一些文件丢失了，并且不确定它们是什么时候被删除的，也不知道如何恢复它们。你的任务是使用 Git 来查找仓库中任何丢失的文件和提交记录。

1. 克隆 `git-playground` 仓库：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 导航到该目录并配置身份：

```shell
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

3. 创建并切换到名为 `one-branch` 的分支，删除 `file2.txt` 并提交，提交消息为 "Remove file2"：

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
```

4. 切换回 `master` 分支并删除 `one-branch` 分支：

```shell
git checkout master
git branch -D one-branch
```

5. 运行 `git fsck --lost-found` 命令来查找任何丢失的文件和提交记录：

```shell
git fsck --lost-found
```

6. 检查 `.git/lost-found` 目录，查看是否有丢失的文件被恢复：

```shell
ls.git/lost-found
```

7. 如果找到了任何丢失的文件，请查看它们以确定是否是丢失的文件。

这是运行 `ls.git/lost-found` 命令的结果：

```shell
commit
```
