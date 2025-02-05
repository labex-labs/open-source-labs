# 查看仓库的可视化图形

作为一名开发者，你可能需要查看仓库的历史记录，以了解代码随时间的变化情况。然而，仅仅查看提交列表可能会让人应接不暇且难以理解。这就是 Git 图形发挥作用的地方。通过可视化仓库的历史记录，你可以快速了解代码是如何演变的，并识别可能引入的任何问题或错误。

要查看 Git 仓库的可视化图形，你可以使用带有 `--graph` 选项的 `git log` 命令。例如，假设你想查看 GitHub 上 `git-playground` 仓库的历史记录。

克隆仓库后，你可以导航到该目录并使用 `git log` 命令查看图形：

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

这将显示仓库中所有提交和分支的可视化图形，让你能够看到代码随时间的演变情况。

这是最终结果：

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
