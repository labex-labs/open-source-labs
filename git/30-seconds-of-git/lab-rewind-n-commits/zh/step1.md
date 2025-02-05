# 回退提交

作为一名开发者，你一直在处理一个项目并进行了多次提交。然而，你意识到最近的几次提交包含错误，你需要回到代码的先前版本。你需要使用 Git来回退你的提交并回到代码的先前版本。

要完成这个实验，你将使用你 GitHub 账户中的 Git 仓库 `git-playground`，它是从 `https://github.com/labex-labs/git-playground.git` 派生而来的。请按照以下步骤操作：

1. 将仓库克隆到你的本地机器：

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. 创建一个名为 `rewind-commits` 的新分支：

```shell
git checkout -b rewind-commits
```

3. 查看仓库的提交历史记录，并意识到最后一次提交包含错误，你需要回到代码的先前版本：

```shell
git log
```

4. 使用 Git 将你的提交回退一次：

```shell
git reset HEAD~1 --hard
```

5. 验证你是否已成功回退提交：

```shell
git log
```

6. 将你的更改推送到 `rewind-commits` 分支：

```shell
git push --force origin rewind-commits
```

这是最终结果：

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
