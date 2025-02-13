# 自动创建上游分支

作为一名开发者，你希望在推送时自动创建上游分支，以避免在远程仓库上手动创建分支的麻烦。

## 任务

为了完成这个挑战，你将使用你 GitHub 账户中的 `git-playground` 仓库，从 `https://github.com/labex-labs/git-playground.git` 的一个分支在推送时自动创建一个上游分支。

1. 克隆仓库，导航到该目录并配置身份。
2. 在推送时启用自动上游分支创建。
3. 创建并切换到一个名为 `new-feature` 的分支，添加 `hello.txt` 文件并在其中写入 "hello,world"，将其添加到暂存区并使用消息 "Added hello.txt" 提交。
4. 将你的更改推送到一个名为 `new-feature` 的新分支，该分支在远程仓库中不存在。

这是完成挑战后的结果：

![自动上游分支结果](../assets/challenge-automatic-push-upstream-step1-1.png)
