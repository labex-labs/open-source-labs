# 切换回上一个分支

作为一名开发者，你正在处理一个项目，并且已经切换到一个不同的分支来开发一个新功能。在进行了一些更改之后，你意识到需要切换回上一个分支来修复一个漏洞。你可以在一个新分支中提交你的更改，然后使用一个命令快速切换回上一个分支。

为了演示如何切换回上一个分支，我们将使用名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库。请按照以下步骤操作：

1. 使用以下命令克隆仓库：
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. 切换到仓库目录：
   ```
   cd git-playground
   ```
3. 创建一个名为 `feature-branch` 的新分支：
   ```
   git checkout -b feature-branch
   ```
4. 检查当前分支并快速切换回上一个分支。你的新分支名为 `feature-branch`，你想要切换回的上一个分支名为 `master`：
   ```
   git checkout -
   ```
   这将切换回 `master` 分支，并且你的更改仍然会保留在那里。
