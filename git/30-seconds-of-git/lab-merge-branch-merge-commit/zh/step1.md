# 合并分支并创建合并提交

作为一名开发者，你可能需要将一个分支合并到当前分支，并创建一个合并提交。如果你不熟悉 Git，这可能会有点棘手。问题是要使用名为 `https://github.com/labex-labs/git-playground` 目录的 Git 仓库，将一个分支合并到当前分支，并创建一个合并提交。

对于这个挑战，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 从 `https://github.com/labex-labs/git-playground.git` 克隆一个仓库：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 导航到该目录并配置身份：

```shell
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

3. 创建并切换到一个名为 `feature-branch` 的分支：

```shell
git checkout -b feature-branch
```

4. 将“这是新的一行。”添加到 `README.md` 文件，将其添加到暂存区并提交，提交消息为“向 README.md 添加新行”：

```shell
echo "这是新的一行。" >> README.md
git add.
git commit -am "向 README.md 添加新行"
```

5. 切换到 `master` 分支：

```shell
git checkout master
```

6. 将 `feature-branch` 合并到 `master` 分支，这将创建一个消息为“合并 feature-branch”的合并提交：

```shell
git merge --no-ff -m "合并 feature-branch" feature-branch
```

这是运行 `git log` 的结果：

```shell
[object Object]
```
