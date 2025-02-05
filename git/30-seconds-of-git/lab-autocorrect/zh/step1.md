# 自动纠正 Git 命令

问题在于开发者经常输错 git 命令，这可能会导致错误并减慢他们的工作流程。例如，开发者可能会不小心输入 `git sttaus` 而不是 `git status`，这将导致错误消息。这可能会令人沮丧且耗时，尤其是在处理包含许多文件和协作者的大型项目时。

为了演示如何使用 Git 的自动纠正功能，我们将使用名为 `https://github.com/labex-labs/git-playground` 目录的 git 仓库。

1. 打开你的终端并导航到你想要克隆仓库的目录。
2. 使用以下命令克隆仓库：

```
git clone https://github.com/labex-labs/git-playground.git
```

3. 使用以下命令导航到克隆的仓库：

```
cd git-playground
```

4. 使用以下命令启用 Git 的自动纠正功能：

```
git config --global help.autocorrect 1
```

5. 尝试输错一个 git 命令，比如 `git sttaus`。Git 将自动纠正该命令并改为运行 `git status`。

这是完成实验后的结果：

![Git 自动纠正命令结果](../assets/challenge-autocorrect-step1-1.jpg)
