# 查找不包含特定提交的分支

你正在处理一个有多个分支的项目，并且需要找到所有不包含特定提交的分支。如果你想确保某个更改已应用于所有分支，或者想知道哪些分支已过时需要更新，这会很有用。

对于本实验，我们将使用名为 `https://github.com/your-username/git-playground` 的 Git 仓库。

1. 使用以下命令将此仓库克隆到你的本地机器：

```shell
git clone https://github.com/your-username/git-playground.git
```

2. 克隆仓库后，使用以下命令导航到该目录并配置身份：

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. 创建并切换到 `new-branch` 分支，在该分支上进行一些代码更改，然后提交，提交消息为 “Create a new-branch branch”：

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. 查看提交消息为 “Create a new-branch branch” 的提交哈希值：

```shell
git log
```

5. 查找所有不包含提交消息为 “Create a new-branch branch” 的哈希值的分支。为此，我们可以使用以下命令：

```shell
git branch --no-contains 31c5ac20129151af1
```

这将输出所有不包含指定提交的分支列表。在这种情况下，输出将是：

```shell
master
```

这意味着 `master` 分支不包含哈希值为 `31c5ac20129151af1` 的提交。
