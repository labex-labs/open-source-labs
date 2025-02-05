# 创建空提交

你需要在你的 Git 存储库中创建一个空提交。这在几种情况下可能会很有用，例如：

- 触发构建过程
- 创建一个占位符提交
- 在存储库的历史记录中标记一个特定点

对于本实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的存储库：

1. 使用命令 `git clone https://github.com/labex-labs/git-playground` 将存储库克隆到你的本地机器。
2. 使用命令 `cd git-playground` 导航到存储库的目录，并使用命令 `git config --global user.name "你的用户名"` 和 `git config --global user.email "你的邮箱"` 在环境中配置你的 GitHub 账户。
3. 使用命令 `git commit --allow-empty -m "Empty commit"` 创建一个消息为 "Empty commit" 的空提交。
4. 使用命令 `git log --name-status HEAD^..HEAD` 验证空提交是否已创建。

这是你运行 `git log --name-status HEAD^..HEAD` 后的结果：

![git log 空提交结果](../assets/challenge-create-empty-commit-step1-1.png)
