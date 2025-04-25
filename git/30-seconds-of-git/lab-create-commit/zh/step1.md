# 创建 Git 提交

你已经对你的代码做了一些修改，并希望将它们作为快照保存在你的 Git 仓库中。然而，你并不想保存你所做的所有修改，只想保存那些与当前功能或错误修复相关的修改。你如何创建一个只包含相关修改的提交呢？

对于本实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库，按照以下步骤操作：

1. 克隆仓库并进入该目录：

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. 在环境中配置你的 GitHub 账户：

   ```
   git config --global user.name "你的名字"
   git config --global user.email "你的邮箱"
   ```

3. 将“hello,labex”添加到 `README.md` 文件中，将其添加到暂存区并使用消息“更新 README.md”提交：

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Update README.md"
   ```

   `-m` 选项允许你指定提交消息。确保消息具有描述性，并解释提交包含哪些更改。

这是运行 `git log` 命令的结果：

![git log 命令输出](../assets/challenge-create-commit-step1-1.png)
