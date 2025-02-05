# 恢复已删除的文件

你正在使用 Git 处理一个项目，不小心删除了你需要的名为 `file2.txt` 的文件。幸运的是，你知道该文件被删除时所在的提交。你的任务是使用 Git 恢复已删除的文件。

要完成本实验，你将使用来自 `https://github.com/labex-labs/git-playground.git` 的 Git 仓库 `git-playground`。请按照以下步骤操作：

1. 使用命令 `cd git-playground` 导航到仓库目录。
2. 运行命令 `git log --oneline` 查看提交历史记录。
3. 找到一条提交信息为 “Added file2.txt” 的提交，该提交中删除了文件。
4. 运行命令 `git checkout <commit> -- <file>` 恢复在指定 `<commit>` 中删除的指定 `<file>`。将 `<commit>` 替换为提交哈希，将 `<file>` 替换为已删除文件的名称。

例如，如果文件 `file2.txt` 在提交 `d22f46b` 中被删除，你将运行以下命令：

```shell
git checkout d22f46b -- file2.txt
```

这会将 `file2.txt` 文件恢复到你的本地仓库。

这是运行 `ll` 命令后的结果：

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```
