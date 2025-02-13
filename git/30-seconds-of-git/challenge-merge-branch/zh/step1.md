# 合并分支

你的任务是使用 Git 将一个分支合并到当前分支。你需要切换到目标分支，然后将源分支合并到该目标分支。当你想要将 `feature-branch-A` 分支中的更改合并到项目的 `master` 分支时，这会很有用。

## 任务

对于这个挑战，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到该目录并配置身份信息。
2. 创建一个 `feature-branch-A` 分支。切换到该分支。
3. 在 `file2.txt` 文件中添加 “hello,world”，将其添加到暂存区，并使用消息 “fix file2.txt” 提交。
4. 切换到 `master` 分支。
5. 将 `feature-branch-A` 合并到 `master` 分支。
6. 解决合并过程中可能出现的任何冲突。

这是运行 `git log` 的结果：

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <xiaoshengyunan@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
