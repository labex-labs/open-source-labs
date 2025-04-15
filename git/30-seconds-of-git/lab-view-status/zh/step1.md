# 查看当前状态

作为一名开发者，了解你的 Git 仓库的当前状态非常重要。这包括哪些文件被修改了、哪些文件已暂存待提交以及哪些文件未被跟踪等信息。`git status` 命令以易于阅读的格式提供这些信息。

你的任务是使用 `git status` 命令查看位于 `https://github.com/labex-labs/git-playground` 的 Git 仓库的当前状态。你应该留意命令的输出并尝试理解其含义。

要完成本实验，你需要克隆位于 `https://github.com/labex-labs/git-playground` 的 Git 仓库。

1. 克隆仓库后，导航到仓库的根目录：

```shell
cd git-playground
```

2. 查看 Git 仓库的当前状态：

```shell
git status
```

这将输出工作目录的当前状态。你应该会看到你当前所在的分支、你的分支是否与远程仓库同步，以及任何未跟踪或已修改的文件的相关信息。

输出如下所示：

```shell
[object Object]
```
