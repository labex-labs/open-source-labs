# 列出所有 Git 别名

作为一名开发者，你可能想要列出系统上已设置的所有 Git 别名。这样做有几个原因，比如：

- 检查有哪些可用的别名
- 找出别名映射到哪些命令
- 删除或修改现有的别名

## 任务

假设你有一个名为 `git-playground` 的 Git 仓库，位于 `https://github.com/labex-labs/git-playground`。

你已经设置了以下别名：

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. 在本地机器上导航到这个仓库。
2. 在列出所有 Git 别名时使用 `sed` 命令。

运行该命令将输出：

```shell
st=status
co=checkout
rb=rebase
```
