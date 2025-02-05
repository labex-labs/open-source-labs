# 撤销提交

假设你已经向 Git 仓库提交了一个内容，但后来发现其中有错误。你希望撤销该提交，同时又不重写仓库的历史记录。该怎么做呢？

为了演示如何撤销提交，我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。请按以下步骤操作：

1. 克隆仓库，进入该目录并配置身份信息：
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```
2. 查看提交历史记录：
   ```
   git log
   ```
   你应该会看到一个提交列表，每个提交都有一个唯一标识符（一长串字母和数字）。
3. 选择一条提交信息为 “Added file1.txt” 的提交，并复制其标识符。
4. 使用 `git revert` 命令撤销该提交：
   ```
   git revert <提交>
   ```
   将 `<提交>` 替换为你要撤销的提交的标识符。
5. Git 会打开一个文本编辑器，让你输入提交信息，保持默认信息即可。
6. 保存并关闭文本编辑器。
7. 再次查看提交历史记录：
   ```
   git log
   ```
   你应该会看到一个新的提交，它撤销了原始提交所做的更改。

这是运行 `git log` 命令后的结果：

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
