# 以其他作者身份创建提交

假设你正在与一组开发人员共同处理一个项目，其中一名团队成员对代码进行了一些更改。然而，他们无法亲自提交这些更改，而你需要代表他们进行提交。在这种情况下，你可以使用 `--author` 选项来更改提交作者的姓名和电子邮件。当你需要将提交归功于其他人时，此选项非常有用，例如当你代表正在休假或病假的同事提交代码时。

要以其他作者身份创建提交，你可以使用以下命令：

```shell
git commit -m < 消息 > --author="<姓名> <电子邮件>"
```

假设你正在处理托管在 `https://github.com/labex-labs/git-playground` 仓库中的项目。你对代码进行了一些更改，并且需要代表你的同事 John Doe 提交这些更改，而他本人无法亲自提交。为此，你可以使用以下命令：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "你的电子邮件"
git config --global user.name "你的用户名"
echo "修复网络错误" > README.md
git add.
git commit -m "修复错误" --author="John Doe <john.doe@example.com>"
```

此命令将创建一个新的提交，消息为“修复错误”，并将其归功于 John Doe。

这是最终结果：

![Git 提交作者更改结果](../assets/challenge-commit-set-author-step1-1.png)
