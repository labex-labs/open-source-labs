# 从远程拉取最新更改

你正在与一组开发人员共同处理一个项目，并且需要确保你本地的代码库副本与团队成员所做的最新更改保持一致。要做到这一点，你需要从远程存储库拉取最新更改。

对于本实验，我们将使用名为 `https://github.com/labex-labs/git-playground` 的 Git 存储库。按照以下步骤完成实验：

1. 切换到克隆存储库的目录：

```shell
cd git-playground
```

2. 从远程存储库的 `master` 分支拉取最新更改：

```shell
git pull origin master
```

运行 `git pull` 命令后，你应该会看到一条消息，表明你本地的存储库副本已与远程存储库保持同步。

这是拉取后的结果：

![git pull command output](../assets/challenge-pull-changes-step1-1.png)
