# 恢复已删除的文件

你正在使用 Git 处理一个项目，不小心删除了你需要的名为 `file2.txt` 的文件。幸运的是，你知道该文件被删除时所在的提交。你的任务是使用 Git 恢复已删除的文件。

## 任务

要完成此挑战，你将使用来自 `https://github.com/labex-labs/git-playground.git` 的 Git 仓库 `git-playground`。

1. 找到一个提交，其中删除了一个文件，提交消息为 “添加了 file2.txt”。
2. 通过检出删除之前的提交来恢复已删除的文件。

这会将 `file2.txt` 文件恢复到你的本地仓库。

这是运行 `ll` 命令的结果：

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
