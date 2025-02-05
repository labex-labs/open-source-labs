# 获取当前分支名称

编写一个命令，用于打印 Git 仓库中当前分支的名称。

假设你正在处理存储在 `https://github.com/labex-labs/git-playground` 仓库中的一个项目。你已经对 `README.md` 文件做了一些更改，并想将它们提交到当前分支。然而，在这样做之前，你想确保自己处于正确的分支上。

要检查当前分支，你可以使用以下命令：

```shell
git rev-parse --abbrev-ref HEAD
```

这会将当前分支的名称打印到控制台。例如，如果你当前处于 `master` 分支，输出将是：

```shell
master
```

如果你切换到不同的分支，比如 `feature-branch`，输出会相应改变：

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

这将输出：

```shell
feature-branch
```
