# 变基到另一个分支

作为一名开发者，你正在处理一个有多个分支的项目。你已经在自己的分支上做了一些更改，并希望将这些更改合并到另一个分支中。然而，你不想直接合并分支，因为你希望保持一个干净的线性历史记录。在这种情况下，你可以使用 `git rebase` 命令将你的分支变基到另一个分支上。

对于这个实验，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。按照以下步骤完成实验：

1. 克隆仓库，进入该目录并配置身份信息：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 创建并切换到一个名为 `one-branch` 的分支：

```shell
git checkout -b one-branch
```

3. 在 `README.md` 文件中添加 "hello,world"，将其添加到暂存区并提交，提交信息为 "Added some changes to README.md"：

```shell
echo "hello,world" >> README.md
git add.
git commit -am "Added some changes to README.md"
```

4. 切换到 `master` 分支：

```shell
git checkout master
```

5. 确保你的本地 `master` 分支与远程仓库保持同步：

```shell
git pull
```

6. 将 `one-branch` 变基到 `master` 分支上：

```shell
git rebase one-branch
```

7. 解决变基过程中出现的任何冲突。

这是运行 `git log` 的结果：

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```
