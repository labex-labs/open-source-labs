# 丢弃未跟踪的更改

你正在使用Git处理一个项目，并对工作目录做了一些更改。然而，你意识到不需要这些更改，想要丢弃它们。你想丢弃当前分支的所有未跟踪更改。

要完成本实验，你将使用名为 `https://github.com/labex-labs/git-playground` 的Git仓库。请按以下步骤操作：

1. 导航到仓库目录：

```shell
cd git-playground
```

2. 检查工作目录的状态：

```shell
git status
```

你应该会看到以下输出：

```shell
[object Object]
```

3. 丢弃当前分支的所有未跟踪更改：

```shell
git clean -f -d
```

4. 再次检查工作目录的状态：

```shell
git status
```

你应该会看到以下输出：

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

`git clean -f -d` 命令已丢弃了当前分支的所有未跟踪更改。
