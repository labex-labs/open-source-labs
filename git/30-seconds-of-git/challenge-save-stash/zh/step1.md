# 创建一个 Git 贮藏

作为一名开发者，你可能会遇到这样的情况：你需要切换到不同的分支或处理不同的功能，但还没准备好提交你的更改。你既不想丢失进度，又不想提交不完整或有问题的代码。这时贮藏就派上用场了。

贮藏能让你保存更改而不提交，这样你就可以切换到不同的分支或处理不同的功能。之后，当你准备好继续处理这些更改时，就可以应用贮藏。

## 任务

假设你正在 `git-playground` 仓库的名为 `feature` 的分支上工作，并且想在切换到其他分支之前保存你的更改：

1. 首先，导航到 `git-playground` 目录。
2. 切换到名为 `feature` 的分支。
3. 在 `README.md` 文件中添加一行“Some changes”。
4. 将你的更改保存到一个贮藏，并为该贮藏添加一条描述性消息“My changes”。
5. 切换到另一个分支。
6. 在另一个分支上完成更改后，切换回 `feature` 分支并应用你的贮藏。

这是最终结果：

```shell
stash@{0}: On feature: My changes
```
