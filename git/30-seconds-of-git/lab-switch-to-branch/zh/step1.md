# 切换到分支

你一直在一个名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库中处理一个项目。你的团队创建了一个名为 `feature-1` 的新分支来处理一项新功能。你需要切换到 `feature-1` 分支以继续处理该功能。

1. 克隆 Git 仓库：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 导航到仓库目录：

```shell
cd git-playground
```

3. 列出仓库中的所有分支：

```shell
git branch
```

输出：

```shell
feature-1
* master
```

4. 切换到 `feature-1` 分支：

```shell
git checkout feature-1
```

输出：

```shell
Switched to branch 'feature-1'
```

5. 验证你现在是否在 `feature-1` 分支上：

```shell
git branch
```

输出：

```shell
* feature-1
master
```
