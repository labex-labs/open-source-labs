# 列出所有 Git 别名

作为一名开发者，你可能想要列出系统上已设置的所有 Git 别名。这样做有几个原因，比如：

- 检查有哪些可用的别名
- 了解某个别名映射到哪些命令
- 删除或修改现有的别名

假设你有一个名为 `git-playground` 的 Git 仓库，位于 `https://github.com/labex-labs/git-playground`。

1. 在本地机器上导航到这个仓库：

```shell
cd git-playground
```

2. 设置以下别名：

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. 在列出所有 Git 别名时使用 `sed` 命令：

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

运行该命令将输出：

```shell
st=status
co=checkout
rb=rebase
```
