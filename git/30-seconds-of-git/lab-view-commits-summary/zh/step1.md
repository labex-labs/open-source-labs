# 查看提交的简短摘要

作为一名开发者，你正在参与一个有多个贡献者的项目。你需要查看对该项目所做的所有提交的摘要，以便了解所做的更改并识别任何潜在问题。然而，你不想花费大量时间在所有提交消息中筛选以找到你需要的信息。

要查看对 Git 存储库所做的所有提交的简短摘要，你可以使用 `git log --oneline` 命令。例如，假设你正在处理一个托管在 GitHub 上名为 `git-playground` 的项目。

1. 你可以使用以下命令将存储库克隆到本地机器：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 克隆存储库后，导航到项目目录并运行以下命令以查看所有提交的简短摘要：

```shell
cd git-playground
git log --oneline
```

这将输出对存储库所做的所有提交的列表，以及每个提交消息的简短摘要。例如：

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
