# 查找包含特定提交的分支

你已获得一个名为 `https://github.com/labex-labs/git-playground` 的 Git 仓库。你的任务是找出所有包含提交消息为“Added file2.txt”的哈希值的分支。

1. 切换到仓库目录：

```shell
cd git-playground
```

2. 使用 `git branch --contains` 命令查找所有包含提交消息为“Added file2.txt”的哈希值的分支：

```shell
git branch --contains d22f46b
```

输出结果应为：

```shell
* master
new-branch
new-branch-1
new-branch-2
```
