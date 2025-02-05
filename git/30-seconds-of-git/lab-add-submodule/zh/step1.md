# 添加子模块

你的任务是向一个 Git 仓库添加一个新的子模块。你需要使用 `git submodule add` 命令将上游仓库中的子模块添加到你仓库中的一个本地目录。该命令的语法如下：

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` 是你想要作为子模块添加的上游仓库的 URL 或路径。
- `<local-path>` 是你想在本地仓库中存储子模块的路径。

假设你有一个名为 `my-project` 的 Git 仓库，并且你想将来自 Git 仓库 `https://github.com/labex-labs/git-playground.git` 的子模块添加到你本地仓库中一个名为 `git-playground` 的目录。你可以这样做：

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git./git-playground
```

这是完成本实验后的结果：

![Git 子模块添加结果](../assets/challenge-add-submodule-step1-1.png)
