# 配置 Git 用户信息

你刚刚开始处理一个新项目，并希望为 Git 配置你的用户信息。你希望确保你的姓名和电子邮件地址与你对仓库所做的任何更改相关联。

对于本实验，我们将使用名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库。按照以下步骤为该仓库配置你的用户信息：

1. 使用以下命令克隆仓库：

```
git clone https://github.com/labex-labs/git-playground.git
```

2. 使用以下命令导航到克隆的仓库：

```
cd git-playground
```

3. 使用 `git config` 命令为仓库设置你的用户信息。例如，如果你的电子邮件地址是 `jane.doe@example.com`，你的名字是 `Jane Doe`，你将使用以下命令：

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. 使用以下命令验证你的用户信息是否已正确设置：`git config --list`。你应该分别在 `user.email` 和 `user.name` 键下看到你的电子邮件地址和名字。

这是完成实验后的结果：

![Git 用户配置结果](../assets/challenge-config-user-step1-1.png)
