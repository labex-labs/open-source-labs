# 删除子模块

你有一个包含名为 `sha1collisiondetection` 的子模块的 Git 仓库。你想从你的仓库中删除这个子模块。

## 任务

对于这个挑战，我们将使用名为 `https://github.com/git/git` 的 Git 仓库。这个仓库包含一个名为 `sha1collisiondetection` 的子模块。

要从仓库中删除 `sha1collisiondetection` 子模块，请按照以下步骤操作：

1. 打开你的终端并导航到你的 Git 仓库的根目录。
2. 取消注册 `sha1collisiondetection` 子模块。
3. 删除 `sha1collisiondetection` 子模块的目录。
4. 删除 `sha1collisiondetection` 子模块的工作树。

完成这些步骤后，`sha1collisiondetection` 子模块将从你的 Git 仓库中删除。如果你运行 `git submodule status` 命令，你将不会得到关于该子模块的任何信息。
