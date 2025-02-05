# 删除分支

你在 Git 仓库中创建了一个本地分支，但不再需要它了。你想删除该分支以保持仓库的整洁和有序。

1. 导航到克隆的仓库：

```shell
cd git-playground
```

2. 查看当前分支：

```shell
git branch
```

3. 删除 `feature-1` 分支：

```shell
git branch -d feature-1
```

4. 验证该分支是否已被删除：

```shell
git branch
```

这是运行 `git branch` 命令后的结果：

```
* master
```
