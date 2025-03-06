# 克隆 Git 仓库

要开始探索 Git 的日期范围过滤功能，我们首先需要一个 Git 仓库来进行操作。我们将使用 LabEx 提供的 `git-playground` 仓库。

让我们从克隆仓库开始：

1. 在 LabEx 虚拟机中打开你的终端。

![terminal](../assets/screenshot-20250306-shbu3WrQ@2x.png)

2. 运行以下命令来克隆仓库：

```bash
git clone https://github.com/labex-labs/git-playground
```

你应该会看到类似以下的输出：

```
Cloning into 'git-playground'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

3. 进入仓库目录：

```bash
cd git-playground
```

现在我们已经将仓库克隆到本地机器上，就可以开始探索提交历史了。
