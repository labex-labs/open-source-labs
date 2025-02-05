# 修改最后一次提交的作者

你刚刚向你的 Git 仓库提交了一次更改，但你意识到作者的姓名和电子邮件地址不正确。你想在不改变提交内容的情况下更新作者信息。使用 Git 该如何实现呢？

要修改最后一次提交的作者，你可以使用 `git commit --amend` 命令。这个命令允许你修改 Git 仓库中的最后一次提交。以下是修改作者姓名和电子邮件地址的示例：

1. 将名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库克隆到你的本地机器：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 使用你的 GitHub 账户配置 Git 的身份信息：

```shell
cd git-playground
git config user.email "你的电子邮件"
git config user.name "你的用户名"
```

3. 使用 `git commit --amend` 命令修改最后一次提交的作者并保存内容：

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. 验证作者信息是否已更新：

```shell
git log
```

你应该会看到最后一次提交的作者现在是 `Duck Quackers`：

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
