# 回退到特定提交

作为一名开发者，你可能需要撤销对代码库所做的更改。例如，你可能犯了一个错误，需要回到代码的早期版本。在这个挑战中，你将使用 Git 回退到仓库中的特定提交。

要完成这个实验，你将使用来自 `https://github.com/labex-labs/git-playground.git` 的 Git 仓库 `git-playground`。按照以下步骤完成挑战：

1. 将仓库克隆到你的本地机器：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 导航到该仓库：

```shell
cd git-playground
```

3. 查看仓库的提交历史：

```shell
git log --oneline
```

4. 确保你想要回退到的提交消息是“Initial commit”的提交哈希。
5. 使用命令 `git reset <commit>` 来回退到指定的提交。例如，你想要回退到哈希为 `3050fc0d3` 的提交：

```shell
git reset 3050fc0d3
```

6. 再次查看仓库的提交历史：

```shell
git log --oneline
```

7. 如果你想删除更改并恢复到代码的早期版本，使用命令 `git reset --hard <commit>`。例如，你想删除更改并恢复到哈希为 `c0d30f305` 的提交：

```shell
git reset --hard c0d30f305
```

这是运行 `git log --oneline` 的结果：

```shell
c0d30f305 (HEAD -> master) Initial commit
```
