# 合并分支

你的任务是使用 Git 将一个分支合并到当前分支。你需要切换到目标分支，然后将源分支合并到该目标分支中。当你想要将 `feature-branch-A` 分支中的更改合并到项目的 `master` 分支时，这会很有用。

对于这个实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。按照以下步骤将 `feature-branch-A` 合并到 `master` 分支：

1. 克隆仓库，导航到该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 创建一个 `feature-branch-A` 分支。切换到该分支：

```shell
git checkout -b feature-branch-A
```

3. 在 `file2.txt` 文件中添加 "hello,world"，将其添加到暂存区并使用消息 "fix file2.txt" 提交：

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "fix file2.txt"
```

4. 切换到 `master` 分支：

```shell
git checkout master
```

5. 将 `feature-branch-A` 合并到 `master` 分支：

```shell
git merge feature-branch-A
```

6. 解决合并过程中可能出现的任何冲突。

这是运行 `git log` 的结果：

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
