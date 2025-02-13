# 删除远程分支

有时，你可能需要删除不再需要的远程分支。例如，如果一个功能分支已经合并到主分支中，你可能想要删除远程功能分支以保持仓库的整洁。

## 任务

假设一个名为 `git-playground` 的 GitHub 仓库已从你的 GitHub 账户克隆而来，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。你想要删除不再需要的名为 `feature-branch` 的远程分支。

1. 打开终端并导航到本地仓库目录。
2. 将 `feature-branch` 分支添加到 `origin` 远程仓库。
3. 列出所有远程分支。
4. 在 `origin` 远程仓库上删除 `feature-branch` 远程分支。
5. 验证远程分支是否已被删除。

输出不应包括 `feature-branch` 远程分支：

```
origin/HEAD -> origin/master
origin/master
```
