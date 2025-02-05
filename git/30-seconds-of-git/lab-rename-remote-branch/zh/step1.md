# 重命名远程分支

要完成本实验，你将使用来自你 GitHub 账户的 Git 仓库 `git-playground`，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。派生时请取消选中「仅复制主分支」。

你有一个名为 `https://github.com/your-username/git-playground` 的 Git 仓库。你已经创建了一个名为 `feature-branch` 的分支并将其推送到远程。现在你想在本地和远程都将该分支重命名为 `new-feature-1`。

1. 克隆仓库，导航到该目录并配置身份：
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. 切换到名为 `feature-branch` 的分支：
   ```shell
   git checkout feature-branch
   ```
3. 在本地和远程重命名分支：
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. 验证分支是否已重命名：
   ```shell
   git branch -a
   ```

这是运行 `git branch -a` 的结果：

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
