# 应用贮藏

你正在 `git-playground` 仓库的一个功能分支上工作，并且需要切换到另一个分支来修复一个漏洞。然而，你有一些尚未准备好提交的更改。你想要保存这些更改并切换到另一个分支。完成漏洞修复后，你想要应用贮藏并继续在功能分支上工作。

## 任务

更改已贮藏在 `feature-branch` 分支上，贮藏消息是“my changes”。

1. 切换到 `git-playground` 目录。
2. 切换到 `master` 分支，在修复漏洞后贮藏它，贮藏消息是“fix the bug”。通过将 `file1.txt` 文件的内容更新为“hello,world”来修复漏洞。
3. 切换到 `feature-branch` 分支，查看贮藏列表，并应用信息为“my changes”的贮藏。

这是 `README.md` 文件的内容：

```
# git-playground
Git Playground
some changes
```

你应该会看到贮藏之前所做的更改现在已应用。
