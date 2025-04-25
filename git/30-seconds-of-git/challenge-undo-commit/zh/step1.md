# 撤销提交

假设你已经向 Git 仓库提交了一个更改，但你意识到其中包含一个错误。你希望撤销该提交，同时不重写仓库的历史记录。你该怎么做呢？

## 任务

为了演示如何撤销提交，我们将使用来自 `https://github.com/labex-labs/git-playground` 的仓库。

1. 导航到仓库目录并配置你的 GitHub 身份。
2. 查看提交历史记录。
3. 选择一条消息为“Added file1.txt”的提交，并复制其标识符。
4. 撤销该提交，Git 将打开一个文本编辑器，让你输入提交消息，保持默认消息不变即可。
5. 保存并关闭文本编辑器。
6. 再次查看提交历史记录。

你应该会看到一个新的提交，它撤销了原始提交所做的更改。

这是运行 `git log` 命令的结果：

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
