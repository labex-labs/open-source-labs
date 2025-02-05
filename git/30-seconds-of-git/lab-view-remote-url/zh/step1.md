# 查看远程仓库的URL

作为一名开发者，出于各种原因，你可能需要查看远程仓库的URL，比如排查Git配置问题或者确认你正在使用正确的仓库。然而，如果你不熟悉Git命令，要知道如何查看远程URL可能会是一项挑战。

在这个实验中，我们将使用名为 `https://github.com/labex-labs/git-playground` 的Git仓库。要查看这个仓库的远程URL，请按照以下步骤操作：

1. 打开你的终端或命令提示符。
2. 导航到你克隆了 `git-playground` 仓库的目录：

```shell
cd git-playground
```

3. 运行以下命令来查看远程URL：

```shell
git config --get remote.origin.url
```

输出应该会显示远程仓库的URL，在这种情况下是 `https://github.com/labex-labs/git-playground.git`。
