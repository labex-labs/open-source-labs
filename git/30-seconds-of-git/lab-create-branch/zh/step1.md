# 创建新分支

对于本实验，请将名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库复刻到你的 GitHub 账户中。你正在名为 `https://github.com/your-username/git-playground` 的 Git 仓库中处理一个项目。你需要创建一个名为 `feature-1` 的新分支来处理一项新功能。

1. 克隆仓库，导航到该目录并配置身份信息：

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 检查当前分支：

```shell
git branch
```

3. 创建一个名为 `feature-1` 的新分支：

```shell
git checkout -b feature-1
```

4. 验证你现在是否位于 `feature-1` 分支上：

```shell
git branch
```

5. 将更改推送到远程仓库：

```shell
git push -u origin feature-1
```

这是你运行 `git branch -r` 命令时的输出结果：

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
