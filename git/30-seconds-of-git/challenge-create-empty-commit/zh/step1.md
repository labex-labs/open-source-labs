# 创建空提交

你需要在你的 Git 仓库中创建一个空提交。这在几种情况下会很有用，例如：

- 触发构建过程
- 创建一个占位提交
- 在仓库历史中标记一个特定点

## 任务

对于这个挑战，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到仓库目录并在环境中配置你的 GitHub 身份。
2. 创建一个消息为「Empty commit」的空提交。
3. 验证空提交是否已创建。

这是你运行 `git log --name-status HEAD^..HEAD` 后的结果：

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
