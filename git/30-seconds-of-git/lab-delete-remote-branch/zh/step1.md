# 删除远程分支

有时，你可能需要删除不再需要的远程分支。例如，如果一个功能分支已经合并到主分支中，你可能想要删除远程功能分支以保持仓库的整洁。

假设一个名为 `git-playground` 的 GitHub 仓库已从你的 GitHub 账户克隆而来，它源自 `https://github.com/labex-labs/git-playground.git` 的一个分支。你想要删除不再需要的名为 `feature-branch` 的远程分支。以下是删除远程分支的步骤：

1. 克隆仓库，导航到该目录并配置身份：
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. 将 `feature-branch` 分支添加到 `origin` 远程仓库：
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. 使用 `git branch -r` 命令列出所有远程分支。
   ```shell
   git branch -r
   ```
   输出应包括 `feature-branch` 远程分支：
   ```
   origin/HEAD -> origin/master
   origin/feature-branch
   origin/master
   ```
4. 使用 `git push -d <remote> <branch>` 命令删除给定 `<remote>` 上指定的远程 `<branch>`。
   ```shell
   git push -d origin feature-branch
   ```
   此命令会删除 `origin` 远程仓库上的 `feature-branch` 远程分支。
5. 再次使用 `git branch -r` 命令验证远程分支是否已被删除。
   ```shell
   git branch -r
   ```
   输出不应包括 `feature-branch` 远程分支：
   ```
   origin/HEAD -> origin/master
   origin/master
   ```
