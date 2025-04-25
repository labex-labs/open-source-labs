# 更改最后一次提交的消息

假设你刚刚将一些更改提交到了你的 Git 仓库，但你意识到提交消息中出现了一个拼写错误。你想在不更改实际所做更改的情况下纠正这个错误。你该怎么做呢？

为了演示如何更改最后一次提交的消息，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。请按照以下步骤操作：

1. 克隆仓库，导航到该目录并配置身份：
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "你的用户名"
   git config --global user.email "你的邮箱"
   ```
2. 将最后一次提交的消息更正为“修复网络错误”：
   ```
   git commit --amend -m "Fix the network bug"
   ```
   这将打开你的默认文本编辑器，你可以在其中修改提交消息。保存并关闭编辑器以完成此过程。
3. 验证提交消息是否已更改：
   ```
   git log --oneline
   ```

你应该在日志中看到更新后的提交消息：

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
