# 创建一个Git暂存区

作为一名开发者，你可能会遇到这样的情况：你需要切换到不同的分支或处理不同的功能，但还没准备好提交你的更改。你既不想丢失你的进度，又不想提交不完整或有问题的代码。这时，暂存区就派上用场了。

暂存区允许你保存更改而不提交，这样你就可以切换到不同的分支或处理不同的功能。之后，当你准备好继续处理你的更改时，就可以应用暂存区的内容。

要创建一个暂存区，你可以使用 `git stash save` 命令。假设你正在 `git-playground` 仓库的一个名为 `feature` 的分支上工作，并且想在切换到其他分支之前保存你的更改：

1. 首先，导航到 `git-playground` 目录：

```shell
cd git-playground
```

2. 切换到名为 `feature` 的分支：

```shell
git checkout -b feature
```

3. 对目录中的文件进行一些更改：

```shell
echo "Some changes" >> README.md
```

4. 将你的更改保存到暂存区：

```shell
git stash save "My changes"
```

5. 切换到另一个分支：

```shell
git checkout master
```

6. 在另一个分支上完成更改后，切换回 `feature` 分支并应用你的暂存区：

```shell
git stash apply
```

这是最终结果：

```shell
stash@{0}: On feature: My changes
```
