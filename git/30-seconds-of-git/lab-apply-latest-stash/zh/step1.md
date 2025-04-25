# 应用最新贮藏

你正在你的 Git 仓库中处理一个项目，并进行了一些尚未准备好提交的更改。然而，你需要切换到另一个分支或提交来处理不同的功能。你不想丢失你的更改，所以决定贮藏它们。之后，当你准备好继续处理更改时，需要将最新的贮藏应用到你的工作目录。

要将最新的贮藏应用到你的 Git 仓库，请按以下步骤操作：

1. 将名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库克隆到你的本地机器。
2. 导航到 `git-playground` 目录。
3. 对 `README.md` 文件进行一些更改，例如在 `README.md` 文件中写入“This is a new line”。
4. 运行命令 `git stash` 来贮藏你的更改。
5. 运行命令 `git stash list` 查看你的贮藏列表。你应该会在列表中看到一个贮藏。
6. 运行命令 `git stash apply` 将最新的贮藏应用到你的工作目录。
7. 检查 `README.md` 文件，查看你的更改是否已应用。

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

这是运行 `cat README.md` 的结果：

```shell
# git-playground
Git Playground
This is a new line
```
