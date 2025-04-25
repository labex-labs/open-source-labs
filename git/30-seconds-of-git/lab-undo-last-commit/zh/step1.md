# 撤销最后一次提交

你刚刚将更改提交到了你的 Git 仓库，但你意识到自己犯了一个错误。你想撤销最后一次提交，同时又不丢失你所做的任何更改。你该怎么做呢？

对于本实验，让我们使用来自 `https://github.com/labex-labs/git-playground` 的仓库。请按照以下步骤操作：

1. 克隆仓库，导航到该目录并配置身份：

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

2. 查看提交历史记录：

```shell
git log
```

3. 撤销最后一次提交，使用该提交更改的反向操作创建一个新的提交：

```shell
git revert HEAD
```

4. 再次查看提交历史记录：

```shell
git log
```

这是运行 `git log --oneline` 命令的结果：

```shell
532b49b (HEAD -> master) 撤销 "添加了 file2.txt"
d22f46b (origin/master, origin/HEAD) 添加了file2.txt
cf80005 添加了file1.txt
b00b937 初始提交
```
