# Git 挑选提交

作为一名开发者，你正在处理一个有多个分支的项目。你发现了之前一次提交中所做的特定更改，并且希望将其应用到你当前的分支上。然而，你并不想合并整个分支，因为其中包含了你不需要的其他更改。在这种情况下，你可以使用 `git cherry-pick` 命令将特定更改应用到你当前的分支。

对于本次实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。按照以下步骤完成挑战：

1. 克隆仓库，进入该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 创建并切换到一个名为 `one-branch` 的分支，创建一个名为 `hello.txt` 的文件，在其中写入 "hello,world"，将其添加到暂存区并提交，提交消息为 "add hello.txt"：

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. 确定上一步中创建的提交的哈希值，以便应用到 `master` 分支：

```shell
git log
```

4. 检出 `master` 分支，并将更改应用到 `master` 分支：

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. 验证更改是否已应用到 `master` 分支：

```shell
git log
```

这是在 `master` 分支上运行 `git log` 的结果：

```shell
ADD hello.txt
```
