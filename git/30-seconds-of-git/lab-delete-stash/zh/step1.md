# 删除 Git 贮藏

你有一个名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库。你已经使用命令 `git stash save "my stash"` 创建了一个贮藏。现在，你想删除这个贮藏，因为你不再需要它了。

1. 使用命令 `cd git-playground` 切换到仓库目录。
2. 使用命令 `git stash list` 列出所有贮藏。你应该会看到你刚刚创建的贮藏。
3. 使用命令 `git stash drop stash@{0}` 删除贮藏。
4. 再次使用命令 `git stash list` 列出所有贮藏。

你刚刚删除的贮藏应该不再显示在列表中。
