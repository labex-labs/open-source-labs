# 查看提交之间的更改

作为一名开发者，你一直在处理托管在 `https://github.com/labex-labs/git-playground` 仓库中的项目。你已经对该仓库进行了多次提交，并且想要查看两个特定提交之间的更改摘要。然而，你不确定如何使用 Git 来做到这一点。

要查看两个提交之间的更改摘要，假设你想要查看 `HEAD` 提交和带有 "Initial commit" 消息的提交之间的更改。以下是你可以做到这一点的方法：

1. 打开一个终端窗口，并导航到 `git-playground` 仓库所在的目录：

```
cd git-playground
```

2. 运行以下命令：

```
git shortlog 3050fc0de..HEAD
```

Git 将显示两个提交之间的更改摘要。你可以使用箭头键浏览摘要，并按 `Q` 退出。

以下是输出可能的样子的示例：

```shell
Hang (2):
      Added file1.txt
      Added file2.txt
```

在这个示例中，Git 显示在 `3050fc0de` 提交和 `HEAD` 提交之间有两个提交。第一个提交添加了 `file1.txt`，第二个提交添加了 `file2.txt`。
