# 修改最后一次提交的作者

你刚刚向你的 Git 仓库提交了一次更改，但你意识到作者的姓名和电子邮件地址不正确。你想在不更改提交内容的情况下更新作者信息。使用 Git 该如何实现呢？

## 任务

要更改最后一次提交的作者，你可以使用一个命令。这个命令允许你修改 Git 仓库中的最后一次提交。

1. 进入仓库，并使用你的 GitHub 账户配置 Git 的身份信息。
2. 将最后一次提交的作者更改为「Duck Quackers」，其电子邮件地址为「cool.duck@qua.ck」，并保存内容。
3. 验证作者信息是否已更新。

你应该会看到最后一次提交的作者现在是「Duck Quackers」：

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
