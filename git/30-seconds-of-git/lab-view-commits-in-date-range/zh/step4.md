# 使用相对日期和格式化选项

Git 还支持相对日期，这对于快速查看近期活动非常方便。

让我们查看过去 12 周内的所有提交：

```bash
git log --since='12 weeks ago'
```

根据你运行此命令的时间，如果你在该时间段内有提交，你可能会看到所有提交，或者只看到其中一部分。

其他有用的相对日期格式包括：

- `"X days ago"`
- `"X months ago"`
- `"yesterday"`
- `"last week"`

让我们尝试查看过去一年的提交：

```bash
git log --since='1 year ago'
```

此命令将显示过去一年中所做的所有提交。

## 额外的格式化选项

`git log` 提供了各种格式化选项来定制输出。以下是一些有用的选项：

1. 要显示更简洁的日志，每个提交显示在一行中：

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

输出将如下所示：

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. 要查看每次提交中更改的文件：

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

此命令显示每次提交中修改的文件的状态，这有助于你了解具体做了哪些更改。

这些格式化选项可以与日期过滤器结合使用，以创建强大的查询，帮助你更有效地了解项目的历史。
